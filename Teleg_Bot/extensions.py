import json
import requests
from API_token import all_key

class APIException(Exception):
    pass

"""

"""
class ConverterValue:
    @staticmethod
    # Используется "-> float" чтобы можно было умножить соотношение валюты на указанное кол-во
    # Так же используется команда "capitalize()" чтобы введеное значение всегда начиналось записывать с заглавной буквы.
    def get_price(quote: str, base: str, amount: str)->float:
        if quote.lower() == base.lower():
            raise APIException(f'Перевод одинаковой валюты не возможен')
        try:
            quote_ticker = all_key[quote.capitalize()]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote_ticker}')
        try:
            base_ticker = all_key[base.capitalize()]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base_ticker}')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')
        url = f'https://min-api.cryptocompare.com/data/price?fsym={all_key[quote]}&tsyms={all_key[base]}'
        r = requests.get(url)
        total_base = json.loads(r.content)[all_key[base]]
        return (total_base * amount)