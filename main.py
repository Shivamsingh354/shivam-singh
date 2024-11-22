import random

"""


stone = -1
paper  = 1
sizzers = 0

stone , paper , scizzers  game

"""

computer = random.choice([-1, 1, 0])
yourturn = input("Enter your choice: ")
yourdict = {"s": -1, "p": 1, "sc": 0}
reversedict = {-1: "stone ",1: "paper", 0: "scizzers"}

you = yourdict[yourturn]

print(f"You choose {reversedict[you]}\ncomputer choose {reversedict[computer]} ")
if(computer == you):
    print("It's a Draw")

else:
    if(computer == -1 and you == 1):
        print("You won")

    elif(computer == -1 and you == 0):
        print("You lose")

    elif(computer == 1 and you == -1):
        print("You lose")

    elif(computer == 1 and you == 0):
        print("You won")

    elif(computer == 0 and you == 1):
        print("You lose")

    elif(computer == 0 and you == -1):
        print("You won")
