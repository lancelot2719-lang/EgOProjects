"""Keyboard walk-through of chapter 6 questions (Russian UI strings).

    python3 -m http.server 8765 -d site &
    uv run --with playwright tools/vlast-golosa/e2e_ch06.py
"""
import asyncio, os
from playwright.async_api import async_playwright
URL = os.environ.get("URL", "http://localhost:8765/vlast-golosa/ch06/")


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=["--autoplay-policy=no-user-gesture-required"])
        pg = await b.new_page(viewport={"width": 1440, "height": 900})
        errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.on("console", lambda m: m.type == "error" and errs.append(m.text))
        await pg.goto(URL); await pg.wait_for_timeout(400)
        ev = pg.evaluate

        async def keys(*ks):
            for k in ks:
                await pg.keyboard.press(k); await pg.wait_for_timeout(80)

        async def at(name):
            i = await ev(f"BEATS.findIndex(b => b.id === '{name}')")
            await ev(f"seek({i}, true)"); await pg.wait_for_timeout(300)
            return i

        fb = lambda: pg.inner_text(".card .fb")
        score = lambda k: ev(f"SCORE['{k}'] && SCORE['{k}'].right")
        await keys("Space"); await pg.wait_for_timeout(1200)
        assert await ev("P.playing && P.t > .3"), "lesson plays"

        i = await at("q1")                      # wrong, then right
        await keys("1"); assert "Не совсем" in await fb(); assert await score("c-cycles") == 0
        await keys("2"); assert "Верно" in await fb()
        await keys("Enter"); assert await ev("P.i") == i + 1

        await at("q3")                          # grid: answer every row correctly
        for k in ["1", "3", "3", "1", "2"]:   # single choice per row: the cursor advances itself
            await keys(k)
        await keys("Enter"); assert "Верно" in await fb(), await fb()
        assert await score("c-keys") == 5

        await at("final1")
        await keys("2"); assert "Верно" in await fb()
        await keys("Enter")
        await pg.keyboard.type("1000"); await keys("Enter"); assert "Верно" in await fb(), await fb()
        await keys("Escape", "Enter")
        await keys("1"); assert "Не совсем" in await fb()
        await keys("s"); assert "Ответ" in await fb()
        await keys("Enter"); await pg.wait_for_timeout(300)

        await at("finish")
        assert "глава 6 пройдена" in (await pg.inner_text(".card")).lower()
        for j in range(await ev("BEATS.length")):  # every beat rebuilds without errors
            await ev(f"seek({j}, false)")
        assert not errs, errs
        print("ch06 keyboard walk-through passed")
        await b.close()

asyncio.run(main())
