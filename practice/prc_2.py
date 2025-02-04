import random

def game():
    print("you are playing the game ")
    score = random.randint(1,100)
    print(f"the score is {score}")
    with open("scores.txt", "r") as file:
        hiscores = file.read()
        if hiscores != "":
            hiscores = int(hiscores)
        else:
            hiscores = 0
    if score > hiscores:
        print("you have beaten the high score")
        with open("scores.txt", "w") as file:
            file.write(str(score))

game()