import GuessGame
import MemoryGame
import CurrencyRuoletteGame
from Score import add_score


def load_game(name):
    difficulty = None
    choose = None
    print(
        f"{name} Please select a game to play:\n1.Memory Game - a sequance of numbers will appear for 1 second and you have to guess it back\n2.Guess Game - guess a number and see if you chose like the computer\n3.Currency Roulette - try and guess the value of a random amount of USD in ILS")
    game_list = {1: MemoryGame.play, 2: GuessGame.play, 3: CurrencyRuoletteGame.play}
    got_choose = False
    while not got_choose:
        choose = int(input("please enter game number between 1 - 3: "))
        if 0 < choose < 4:
            print(f"you choose Game number {choose}: ")
            break
        else:
            print("the number you entered is incorrect")
    got_diff = False
    while not got_diff:
        try:
            difficulty = int(input("Please choose the game difficulty level between 1 - 5: "))
            if 0 < difficulty < 6:
                print(f"you choose Difficulty level {difficulty}")
                got_diff = True
            else:
                print("you entered a wrong number")
        except ValueError:
            print("you entered a non number value")
    win = game_list[choose](difficulty)
    print(win)
    if win:
        add_score(difficulty)
    return difficulty



def welcome():
    name = input("Please enter your name: ")
    print(f"Hello {name} and welcome to the World of Games (WoG). \nHere you can find many cool games to play.")
    difficulty = load_game(name)
    return name, difficulty


if __name__ == '__main__':
    welcome()
