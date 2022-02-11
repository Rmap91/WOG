import random
from sys import stdout
from time import sleep

def Show1(list):
    for s in list:
        stdout.write("%d " % s)
    sleep(.7)
    stdout.write("\r")
    stdout.flush()

def generate_sequence(difficulty):
    list = [random.randrange(1, 101) for i in range(difficulty)]
    return list

def get_list_from_user():
    stdout.flush()
    user = (input(f"please enter the numbers you saw: "))
    return user

def is_list_equal(list, user):
    string = ' '.join([str(i) for i in list])
    userARR = ' '.join([str(i) for i in user.split()])
    return string.strip() == userARR.strip()

def play(difficulty = None):
    if difficulty is None:
        difficulty = int(input(f"please enter a difficulty level: "))
    generated_list = generate_sequence(difficulty)
    Show1(generated_list)
    user = get_list_from_user()
    return is_list_equal(generated_list, user)


