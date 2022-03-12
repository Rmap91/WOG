from live import welcome
from Score import add_score


def maingame():
    name, difficulty = welcome()
    add_score(difficulty)




if __name__ == '__main__':
    maingame()


