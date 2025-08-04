# CurrencyExchangeBot

Простой Telegram-бот (@loweqa_bot), который позволяет конвертировать валюту с использованием API CoinDesk(https://developers.coindesk.com/documentation/legacy/Price/SingleSymbolPriceEndpoint).

# Создание Telegram-бота

Наберите в ТГ @BotFather и следуйте инструкциям:
```/newbot```

Узнать подробности можно здесь: https://core.telegram.org/bots#6-botfather

## Установка
```bash
git clone https://github.com/YuliyaKhrushchova/CurrencyExchangeBot.git
cd CurrencyExchangeBot
pip install -r requirements.txt
```

Добавьте токен, полученный при создании бота, вручную в файл config.py:
```
BOT_TOKEN=ваш_токен
```

Запустите app.py:
```bash
python3 app.py
```

## Использование
- `/start` — начать работу с ботом
- `/help` — справка
- `/currencies` - список доступных валют
- `/add` - добавить новую валюту
- `доллар злотый 100` - перевести 100 долларов в злотые