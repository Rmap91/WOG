from live import welcome




def add_score(difficulty):
    Points_of_Winning = int((difficulty * 3) + 5)
    try:
        scores = open("Scores.txt", "r")
        score = scores.read().strip()
        print(scores.readline())
        Points_of_Winning += int(score)
    except:
        print("file doesnt exist")
    Points_of_Winning = str(Points_of_Winning)
    scores = open("Scores.txt", "w")
    scores.write(str(Points_of_Winning))
    scores.close()



if __name__ == '__main__':
    name, difficulty = welcome()
    add_score(difficulty)
