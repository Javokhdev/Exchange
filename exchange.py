import requests
import json
import os
from colorama import Fore, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)

def fetch_exchange_rates():
    try:
        response = requests.get('https://nbu.uz/en/exchange-rates/json/')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        print(Fore.RED + "Error fetching exchange rate data. Please check your internet connection and try again.")
        return load_cached_data()

def cache_exchange_rates(data):
    with open("exchange_rates.json", "w") as file:
        json.dump(data, file)

def load_cached_data():
    if os.path.exists("exchange_rates.json"):
        with open("exchange_rates.json", "r") as file:
            return json.load(file)
    print(Fore.RED + "No cached data available. Please connect to the internet and try again.")
    exit()

def get_currency_rate(data, currency):
    for item in data:
        if item['code'].casefold() == currency.casefold():
            return float(item['cb_price'])
    print(Fore.RED + f"Currency '{currency}' not found. Please try again.")
    return None

def display_all_currencies(data):
    print(Fore.YELLOW + "\nAvailable currencies:")
    print(Fore.CYAN + "-" * 40)
    for item in data:
        print(Fore.GREEN + f"{item['code']} - {item['title']}")
    print(Fore.CYAN + "-" * 40)

def main_menu():
    print(Fore.MAGENTA + "\nCurrency Converter")
    print(Fore.CYAN + "=" * 30)
    print(Fore.YELLOW + "1. Check currency rate")
    print(Fore.YELLOW + "2. Convert currency to UZS")
    print(Fore.YELLOW + "3. View all available currencies")
    print(Fore.YELLOW + "4. Exit")
    print(Fore.CYAN + "=" * 30)

def main():
    # Fetch and cache exchange rates
    data = fetch_exchange_rates()
    cache_exchange_rates(data)

    while True:
        main_menu()
        choice = input(Fore.BLUE + "Choose an option (1-4): ").strip()

        if choice == '1':
            currency = input(Fore.BLUE + "\nEnter the currency type (e.g., USD, EUR): ").strip().upper()
            rate = get_currency_rate(data, currency)
            if rate:
                print(Fore.GREEN + f"\nThe current price of '{currency}' is: {rate} UZS")
        elif choice == '2':
            currency = input(Fore.BLUE + "\nEnter the currency type (e.g., USD, EUR): ").strip().upper()
            rate = get_currency_rate(data, currency)
            if rate:
                try:
                    amount = float(input(Fore.BLUE + f"Enter the amount of {currency} to convert: ").strip())
                    converted_amount = rate * amount
                    print(Fore.GREEN + f"\n{amount} {currency} is equivalent to {converted_amount:,.2f} UZS.")
                except ValueError:
                    print(Fore.RED + "Invalid amount entered. Please enter a numeric value.")
        elif choice == '3':
            display_all_currencies(data)
        elif choice == '4':
            print(Fore.CYAN + "\nThank you for using the Currency Converter. Goodbye!")
            break
        else:
            print(Fore.RED + "\nInvalid choice. Please choose a valid option (1-4).")

if __name__ == "__main__":
    main()
