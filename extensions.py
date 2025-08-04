import requests
import json
from utils import currencies


class ExchangeException(Exception):
    pass


class CurrencyExchange:
    @staticmethod
    def convert(from_curr_raw: str, to_curr_raw: str, amount: str):
        if from_curr_raw == to_curr_raw:
            raise ExchangeException("Невозможно конвертировать одинаковые валюты.")

        if from_curr_raw not in currencies:
            raise ExchangeException(f"Валюта '{from_curr_raw}' не поддерживается.")

        if to_curr_raw not in currencies:
            raise ExchangeException(f"Валюта '{to_curr_raw}' не поддерживается.")

        try:
            amount = float(amount)
        except ValueError:
            raise ExchangeException("Не удалось обработать количество.")

        from_curr = currencies[from_curr_raw]
        to_curr = currencies[to_curr_raw]

        url = f"https://min-api.cryptocompare.com/data/price?fsym={from_curr}&tsyms={to_curr}"
        response = requests.get(url)

        if response.status_code != 200:
            raise ExchangeException("Ошибка при запросе к API.")

        rate = json.loads(response.content)[to_curr]

        if rate is None:
            raise ExchangeException("Ошибка в получении курса валют.")

        return rate * amount


class CurrencyAdd:
    @staticmethod
    def add_currency(curr_name_raw: str, curr_code_raw: str):

        curr_name = curr_name_raw.lower()
        curr_code = curr_code_raw.upper()

        if curr_name in currencies:
            raise ExchangeException(f"Валюта '{curr_name}' уже добавлена.")

        url = f"https://min-api.cryptocompare.com/data/price?fsym={curr_code}&tsyms=USD"
        response = requests.get(url)
        if response.status_code != 200:
            raise ExchangeException("Ошибка при запросе к API.")

        check = json.loads(response.content)

        if 'Response' in check:
            raise ExchangeException(f"Валюта '{curr_name}' не существует")

        currencies[curr_name] = curr_code

        return f"Валюта '{curr_name}' с кодом '{curr_code}' добавлена."
