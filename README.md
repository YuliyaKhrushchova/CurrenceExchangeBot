# CurrencyExchangeBot

Простой Telegram-бот (@lrnn_bot), который позволяет конвертировать валюту с использованием API CoinDesk(https://developers.coindesk.com/documentation/legacy/Price/SingleSymbolPriceEndpoint).

# Создание Telegram-бота

Наберите в ТГ @BotFather и следуйте инструкциям:
```/newbot```

Узнать подробности можно здесь: https://core.telegram.org/bots#6-botfather

## Установка
```bash
git clone https://github.com/YuliyaKhrushchova/CurrencyExchangeBot.git
cd currency_exchange_bot
python -m venv venv       # создаёт окружение
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

Добавьте токен вручную в файл config.py:
```
BOT_TOKEN=ваш_токен
```

## Использование
- `/start` — начать работу с ботом
- `/help` — справка
- `/currencies` - список доступных валют
- `/add` - добавить новую валюту
- `доллар злотый 100` - перевести 100 долларов в злотые