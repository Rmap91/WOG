import requests
import random

currency = requests.get("https://freecurrencyapi.net/api/v2/latest?apikey=72f9ee40-8b32-11ec-a979-0158ca326e15&base_currency=USD")
data = currency.json()
conver = (data['data']['ILS'])
gen = (random.randrange(1, 101))
t = int(gen * conver)

def get_money_interval(difficulty):
    total = (t - (5-difficulty), t + (5-difficulty))
    return total

def get_guess_from_user():
    num = int(input("please enter a guess for the total amount: "))
    return num

def play(difficulty = None):
    if difficulty is None:
        difficulty = int(input(f"please enter a difficulty level: "))
    low, high = get_money_interval(difficulty)
    guess = get_guess_from_user()
    s = low < guess < high
    return s



