import os 
import requests
from pprint import PrettyPrinter
from dotenv import load_dotenv

BASE_URL = 'https://v6.exchangerate-api.com/'

load_dotenv()
API_KEY = os.environ.get('EXCHANGE_API_KEY')

printer = PrettyPrinter()

def get_currency():
    endpoint = f'v6/{API_KEY}/latest/USD'
    url = BASE_URL + endpoint

    resp = requests.get(url)
    data = resp.json()
    data = data['conversion_rates']

    return data

def get_exchange_rate(currency, amount, currencies):

    if currency not in currencies:
        return None 
    else:
        return currencies[currency] * amount

def main():
    currency_data = get_currency()

    print("Welcome to the currency converter - USD -> Other Currencies!")
    print()

    while True:
        user_input = input("Type (y/n) to convert our currency OR (list) to view the lists of currencies: ").lower()

        if user_input == 'y':
            curr_sym = input('Please enter your currency symbol: ').upper()
            curr_amt = int(input('Please enter your currency amount in USD: '))
            exchange_rate = get_exchange_rate(curr_sym, curr_amt, currency_data)

            if exchange_rate is None:
                print(f"Sorry, '{curr_sym}' is not a valid currency code.")
            else:
                print(f'Your conversion rate from {curr_amt} USD to {curr_sym} is {exchange_rate} {curr_sym}')

        elif user_input == 'list':
            printer.pprint(currency_data)

        else:
            print("Thank you!")
            break

main()