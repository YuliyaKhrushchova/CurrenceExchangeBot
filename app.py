import telebot

from config import BOT_TOKEN
from extensions import ExchangeException, CurrencyExchange, CurrencyAdd
from utils import help_text, greetings, currencies

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(
    func=lambda message: message.text.startswith('/') and message.text.split()[0][1:] not in ['start', 'help',
                                                                                              'currencies', 'add'])
def handle_unknown_command(message: telebot.types.Message):
    bot.reply_to(message, "Неизвестная команда. Введите /help для списка доступных.")


@bot.message_handler(commands=['start'])
def handle_start(message: telebot.types.Message):
    bot.reply_to(message, greetings + help_text)


@bot.message_handler(commands=['help'])
def handle_help(message: telebot.types.Message):
    bot.reply_to(message, help_text)


@bot.message_handler(commands=['currencies'])
def handle_currencies(message: telebot.types.Message):
    text = "Доступные валюты:\n" + "\n".join(currencies.keys())
    bot.reply_to(message, text)


@bot.message_handler(commands=['add'])
def handle_add_currency(message: telebot.types.Message):
    try:
        args = message.text.split(' ')
        if len(args) != 3:
            raise ExchangeException("Используйте формат: /add <название> <код валюты>")

        command, curr_name_raw, curr_code_raw = args

        response =  CurrencyAdd.add_currency(curr_name_raw, curr_code_raw)

    except ExchangeException as e:
        bot.reply_to(message, f"Ошибка: {e}")
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду /add.\n{e}")
    else:
        bot.reply_to(message, response)


@bot.message_handler(content_types=['text', ])
def handle_conversion(message: telebot.types.Message):
    try:
        values = message.text.lower().split(' ')
        if len(values) != 3:
            raise ExchangeException("Неверный формат запроса. Пример: доллар рубль 100")

        from_curr, to_curr, amount = values
        result = CurrencyExchange.convert(from_curr, to_curr, amount)
        response = f"{amount} {from_curr} = {round(result, 2)} {to_curr}"

    except ExchangeException as e:
        bot.reply_to(message,f"Ошибка: {e}")
    except Exception:
        bot.reply_to(message,f"Не удалось обработать команду. Проверьте данные.")
    else:
        bot.reply_to(message, response)


bot.polling(none_stop=True)
