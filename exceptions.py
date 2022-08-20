import json
import requests
from config import currencies_names


class ConvertingExceptions(Exception):
    pass


class CurrencyConvertor:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        quote, base = quote.lower(), base.lower()
        if quote == base:
            raise ConvertingExceptions(f'Failed to exchange the same currencies {base}.')
        try:
            quote_ticker = currencies_names[quote]
        except KeyError:
            raise ConvertingExceptions(f'Failed to process currency {quote}.')
        try:
            base_ticker = currencies_names[base]
        except KeyError:
            raise ConvertingExceptions(f'Failed to process currency {base}.')
        try:
            amount = float(amount.replace(',', '.'))
        except ValueError:
            raise ConvertingExceptions(f'Failed to process quantity {amount}.')
        if amount <= 0:
            raise ConvertingExceptions(f'Amount cannot be negative or equal to 0.')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}'
                         f'&tsyms={base_ticker}')
        total_base = json.loads(r.content)[currencies_names[base]]
        return total_base * amount
