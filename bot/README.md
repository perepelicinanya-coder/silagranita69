# Telegram-бот «Сила Гранита»

Бот открывается по QR-ссылке:

```text
https://t.me/silagranita69bot?start=stone_guide
```

После нажатия `Запустить` показывает меню:

- рассчитать заказ;
- каталог изделий;
- кухонные столешницы;
- памятники;
- гайд по выбору камня;
- контакты мастера.

## Важно про токен

Токен бота нельзя хранить в коде и нельзя публиковать в GitHub.

Если токен уже был отправлен в чат, перевыпустите его в Telegram через `@BotFather`.

## Локальный запуск на Windows PowerShell

```powershell
cd C:\Users\Руслан\website\bot
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:TELEGRAM_BOT_TOKEN="НОВЫЙ_ТОКЕН_ОТ_BOTFATHER"
python bot.py
```

Пока окно терминала открыто, бот работает.

Для постоянной работы бот нужно разместить на сервере/VPS или настроить как сервис.
