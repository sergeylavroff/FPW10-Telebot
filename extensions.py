import requests
import json
from config import currency


class ConvertionException(Exception):
    pass

class CurrencyConvertor:
    @staticmethod
    def get_price(base, quote, amount):
        if base == quote:
            raise ConvertionException('Невозможно перевести одинаковые валюты!')
        try: base_try = currency[base]
        except KeyError:
            raise ConvertionException(f'Валюта {base} не найдена.')
        try: quote_try = currency[quote]
        except KeyError:
            raise ConvertionException(f'Валюта {quote} не найдена.')
        try: amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')
        values = requests.get(f'https://api.exchangeratesapi.io/latest?symbols={quote_try}&base={base_try}')
        total_base = json.loads(values.content)['rates'][quote_try]
        return format(float(total_base)*amount, ".2f")