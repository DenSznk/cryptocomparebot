import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

currencies_names = {
    'dollar': 'USD',
    'euro': 'EUR',
    'lari': 'GEL',
    'yuan': 'CNY',
    'zloty': 'PLN',
    'hryvnia': 'UAH',
    'poundsterling': 'GBP',
    'bitcoin': 'BTC',
    'ethereum': 'ETH',
    'tether': 'USDT',
    'solana': 'SOL',
    'polkadot': 'DOT',
    'binanceUSD': 'BUSD',
    'polygon': 'MATICK',
}
