import datetime as dt
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

import config
import db
from llm import estimate_macros

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s", level=logging.INFO
)
logger = logging.getLogger("food-bot")

WATER_CALLBACK = "water_tap"

HELP_TEXT = (
    "Я веду дневник питания.\n\n"
    "🍽 Просто напиши, что съел — оценю калории и БЖУ "
    "(нужен запущенный локальный сервер в LM Studio).\n"
    "/today — итоги за сегодня\n"
    "/week — сводка за 7 дней\n"
    "/weight 94.5 — записать вес\n"
    "/water — отметить стакан воды\n"
    "/help — эта справка"
)


async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    db.register_user(update.effective_chat.id)
    await update.message.reply_text("Привет! " + HELP_TEXT)


async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_TEXT)


async def cmd_today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    totals = db.get_today_totals(chat_id)
    water = db.get_water_count_today(chat_id)
    water_target_glasses = round(config.WATER_TARGET_ML / config.WATER_GLASS_ML)
    last_weight = db.get_last_weight(chat_id)

    lines = [
        "📊 Сегодня:",
        f"Приёмов пищи: {totals['entries']}",
        f"Калории: {totals['kcal']:.0f} / {config.TARGET_KCAL} ккал",
        f"Белок: {totals['protein_g']:.0f} / {config.TARGET_PROTEIN_G} г",
        f"Углеводы: {totals['carbs_g']:.0f} г, жиры: {totals['fat_g']:.0f} г",
        f"Вода: {water} / {water_target_glasses} стаканов",
    ]
    if last_weight:
        lines.append(f"Последний вес: {last_weight['weight_kg']} кг ({last_weight['ts'][:10]})")
    await update.message.reply_text("\n".join(lines))


async def cmd_week(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    summary = db.get_week_summary(chat_id)
    lines = [
        "📈 Последние 7 дней:",
        f"Среднее в день: {summary['avg_kcal']:.0f} ккал, {summary['avg_protein']:.0f} г белка",
    ]
    weights = summary["weights"]
    if weights:
        lines.append("Взвешивания:")
        for w in weights:
            lines.append(f"  {w['ts'][:10]}: {w['weight_kg']} кг")
        if len(weights) >= 2:
            diff = weights[-1]["weight_kg"] - weights[0]["weight_kg"]
            lines.append(f"Изменение за период: {diff:+.1f} кг")
    else:
        lines.append("Взвешиваний за неделю пока нет — используй /weight <кг>")
    await update.message.reply_text("\n".join(lines))


async def cmd_weight(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if not context.args:
        last = db.get_last_weight(chat_id)
        if last:
            await update.message.reply_text(
                f"Последний записанный вес: {last['weight_kg']} кг ({last['ts'][:10]}).\n"
                "Чтобы записать новый: /weight 94.2"
            )
        else:
            await update.message.reply_text("Записей веса ещё нет. Пример: /weight 94.2")
        return
    try:
        value = float(context.args[0].replace(",", "."))
    except ValueError:
        await update.message.reply_text("Не понял число. Пример: /weight 94.2")
        return
    db.log_weight(chat_id, value)
    await update.message.reply_text(f"Записал: {value} кг ✅")


def _water_reply_text(count: int) -> str:
    target_glasses = round(config.WATER_TARGET_ML / config.WATER_GLASS_ML)
    return f"💧 Вода сегодня: {count}/{target_glasses} стаканов"


async def cmd_water(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    db.log_water(chat_id)
    count = db.get_water_count_today(chat_id)
    await update.message.reply_text(_water_reply_text(count))


async def on_water_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat_id
    db.log_water(chat_id)
    count = db.get_water_count_today(chat_id)
    await query.answer("Записал 💧")
    await query.edit_message_text(_water_reply_text(count))


async def on_food_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text = update.message.text.strip()
    if not text:
        return

    thinking = await update.message.reply_text("Считаю... ⏳")
    macros = estimate_macros(text)

    if macros is None:
        await thinking.edit_text(
            "Не получилось оценить автоматически (проверь, что в LM Studio запущен "
            "локальный сервер и загружена модель). Запись сохранена без БЖУ."
        )
        db.log_food(chat_id, text, None, None, None, None, None)
        return

    db.log_food(
        chat_id,
        text,
        macros["kcal"],
        macros["protein_g"],
        macros["carbs_g"],
        macros["fat_g"],
        macros["comment"],
    )
    totals = db.get_today_totals(chat_id)
    reply = (
        f"✅ {macros['kcal']:.0f} ккал · Б {macros['protein_g']:.0f} / "
        f"У {macros['carbs_g']:.0f} / Ж {macros['fat_g']:.0f}\n"
    )
    if macros["comment"]:
        reply += f"{macros['comment']}\n"
    reply += (
        f"\nСегодня всего: {totals['kcal']:.0f} / {config.TARGET_KCAL} ккал, "
        f"{totals['protein_g']:.0f} / {config.TARGET_PROTEIN_G} г белка"
    )
    await thinking.edit_text(reply)


async def water_reminder_job(context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("💧 Отметить стакан", callback_data=WATER_CALLBACK)]]
    )
    for chat_id in db.get_all_chat_ids():
        try:
            await context.bot.send_message(chat_id, "Не забудь про воду 💧", reply_markup=keyboard)
        except Exception:
            logger.exception("Не удалось отправить напоминание о воде chat_id=%s", chat_id)


async def weighin_reminder_job(context: ContextTypes.DEFAULT_TYPE):
    for chat_id in db.get_all_chat_ids():
        try:
            await context.bot.send_message(
                chat_id,
                "📅 Пора еженедельно взвеситься — натощак, в одно и то же время.\n"
                "Запиши результат: /weight <кг>",
            )
        except Exception:
            logger.exception("Не удалось отправить напоминание о взвешивании chat_id=%s", chat_id)


def _parse_hhmm(value: str) -> dt.time:
    hour, minute = value.split(":")
    return dt.time(hour=int(hour), minute=int(minute), tzinfo=config.ZONE)


def schedule_jobs(app: Application):
    for time_str in config.WATER_REMINDER_TIMES:
        app.job_queue.run_daily(water_reminder_job, time=_parse_hhmm(time_str))

    app.job_queue.run_daily(
        weighin_reminder_job,
        time=_parse_hhmm(config.WEIGHIN_TIME),
        days=(config.WEIGHIN_DAY,),
    )


def main():
    if not config.BOT_TOKEN:
        raise SystemExit(
            "BOT_TOKEN не задан. Скопируй .env.example в .env и впиши токен от @BotFather."
        )

    db.init_db()

    app = Application.builder().token(config.BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("help", cmd_help))
    app.add_handler(CommandHandler("today", cmd_today))
    app.add_handler(CommandHandler("week", cmd_week))
    app.add_handler(CommandHandler("weight", cmd_weight))
    app.add_handler(CommandHandler("water", cmd_water))
    app.add_handler(CallbackQueryHandler(on_water_button, pattern=f"^{WATER_CALLBACK}$"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_food_text))

    schedule_jobs(app)

    logger.info("Бот запущен, ждёт сообщений...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
