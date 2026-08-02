# Удалённый доступ к OpenCode + проектам

## Схема

```
Ноутбук (где угодно) 
    │ Tailscale (шифрованный P2P-туннель)
    ▼
Домашний ПК (основной)
    │ OpenSSH Server
    ▼
    Терминал → OpenCode → твои проекты
```

Никаких открытых портов в интернет. Tailscale создаёт закрытую сеть между твоими устройствами.

---

## 1. Установка Tailscale (на оба ПК — бесплатно)

**Домашний ПК:**
```powershell
winget install Tailscale.Tailscale
# Или скачай с https://tailscale.com/download
# Войди через Google/Microsoft/GitHub — создастся приватная сеть
```

**Ноутбук:**
То же самое — установи Tailscale, войди в тот же аккаунт.

После входа на обоих — устройства увидят друг друга. Проверь:
```powershell
tailscale status
# Должен показать оба устройства с их IP (вида 100.x.x.x)
```

---

## 2. Включение OpenSSH Server (Домашний ПК)

```powershell
# Проверь, установлен ли OpenSSH
Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH.Server*'

# Если нет — установи:
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

# Включи и запусти
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'

# Разреши в фаерволе
New-NetFirewallRule -DisplayName 'OpenSSH Server' -Profile @('Domain', 'Private', 'Public') -Direction Inbound -Action Allow -Protocol TCP -LocalPort 22
```

Узнай свой Tailscale IP:
```powershell
tailscale ip -4  # что-то типа 100.x.x.x
```

---

## 3. Подключение с ноутбука

```powershell
# Подключись к домашнему ПК через Tailscale
ssh username@100.x.x.x

# username — твой логин в Windows на домашнем ПК
# Пароль — твой пароль от Windows (если настроил ключи — без пароля)
```

После входа — запускай OpenCode:
```powershell
cd D:\AI_Project
opencode
```

---

## 4. (Опционально) Доступ к файлам через SMB

Если хочешь редактировать файлы из ноутбука в VS Code, но гонять OpenCode на домашнем ПК:

На домашнем ПК расшарь папку:
```powershell
New-SmbShare -Name "AI_Project" -Path "D:\AI_Project" -FullAccess Everyone
```

На ноутбуке подключи как сетевой диск:
```powershell
net use Z: \\100.x.x.x\AI_Project
```

Теперь открываешь файлы локально в VS Code, а OpenCode запускаешь через SSH когда нужен AI.

---

## Альтернативы

| Способ | Сложность | Бесплатно? | Особенности |
|---|---|---|---|
| **Tailscale + SSH** | Низкая | ✅ Да (≤100 устройств) | Рекомендую |
| **ZeroTier** | Средняя | ✅ Да | Аналог Tailscale, чуть сложнее |
| **Cloudflare Tunnel** | Высокая | ✅ Да | Нужен свой домен, RDP через браузер |
| **OpenVPN** | Высокая | ✅ Да | Требует серверной настройки |
| **AnyDesk / TeamViewer** | Низкая | ⚠️ Бесплатно с ограничениями | Только удалённый рабочий стол, не терминал |
| **Dropbox/OneDrive** | Низкая | ⚠️ 5-10GB бесплатно | Синхронизация файлов, не терминал |

---

## Быстрый старт (если ничего не установлено)

**Домашний ПК (один раз):**
```powershell
winget install Tailscale.Tailscale
# войти в аккаунт
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'
```

**Ноутбук (один раз):**
```powershell
winget install Tailscale.Tailscale
# войти в тот же аккаунт
```

**Каждый раз с ноутбука:**
```powershell
ssh username@100.x.x.x
cd D:\AI_Project
opencode
```
