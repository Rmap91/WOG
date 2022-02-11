import GuessGame
import MemoryGame
import CurrencyRuoletteGame
def welcome():
    name = input("Please enter your name: ")
    print(f"Hello {name} and welcome to the World of Games (WoG). \nHere you can find many cool games to play.")
welcome()

def load_game():
    print(f"Please select a game to play:\n1.Memory Game - a sequance of numbers will appear for 1 second and you have to guess it back\n2.Guess Game - guess a number and see if you chose like the computer\n3.Currency Roulette - try and guess the value of a random amount of USD in ILS")
    game_list = {1:MemoryGame.play ,2:GuessGame.play ,3:CurrencyRuoletteGame.play}
    while True:
        choose = int(input("please enter game number between 1 - 3: "))
        if  0 < choose < 4:
            print(f"you choose Game number {choose}: ")
            break
        else:
            print(f"the number you entered is incorrect")
    while True:
        difficulty = int(input("Please choose the game difficulty level between 1 - 5: "))
        if 0 < difficulty < 6:
            print(f"you choose Difficulty level {difficulty}")
            break
        else:
            print("you choose an incorrect number")
    print(game_list[choose](difficulty))
load_game()