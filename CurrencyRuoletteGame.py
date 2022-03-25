import random
from currency_converter import CurrencyConverter

c = CurrencyConverter()
gen = int(random.randrange(1, 101))
conver = c.convert(gen,'ILS', 'USD')


def get_money_interval(difficulty):
    total = (conver - (5-difficulty), conver + (5-difficulty))
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



