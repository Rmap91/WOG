import random

def generate_number(difficulty):
    secret_number = random.randint(1,difficulty)
    return secret_number

def get_guess_from_user(difficulty):
     y = int(input(f"please enter your guess between 1 and {difficulty}: "))
     return y

def compare_results(secret_number,y):
    return secret_number == y

def play(difficulty = None):
    if difficulty is None:
        difficulty = int(input(f"please enter a difficulty level: "))
    secret_number = generate_number(difficulty)
    y = get_guess_from_user(difficulty)
    return compare_results(secret_number, y)

