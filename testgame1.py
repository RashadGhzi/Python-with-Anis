
from random import randint
a = 0
cpoint = 0
ppoint = 0
print("Welcome to rock, paper and scissor.")

while a < 3:
    b = ["first", "second", "third"]
    d = b[a]
    print("Your turn:")
    game = ["Rock", "Paper", "Scissor"]
    print("1.Rock. \n2.Paper. \n3.Scissor")

    player = int(input())
    player -= 1
    player1 = game[player]
    print("You choossed "+player1)
    print("Computer turn:")

    computer = randint(0,2)
    computer1 = game[computer]
    print("computer choossed "+computer1)

    if computer == player:
        print("It's a draw. You both win in the "+d,"round.")
        cpoint = cpoint + 1
        ppoint = ppoint + 1
    elif (computer == 1) & (player == 0):
        print("Computer won the "+d,"round.")
        cpoint = cpoint + 1
        ppoint = ppoint + 0
    elif (computer == 0) & (player == 2):
        print("Computer won the "+d,"round.")
        cpoint = cpoint + 1
        ppoint = ppoint + 0
    elif (computer == 2) & (player == 1):
        print("Computer won the "+d,"round.")
        cpoint = cpoint + 1
        ppoint = ppoint + 0
    else:
        print("Player won the "+d,"round.")
        ppoint = ppoint + 1
        cpoint = cpoint + 0

    print("Computer point is ", +cpoint)
    print("Player point is ", +ppoint)
    print("\n")
    a = a + 1

if cpoint == ppoint:
    print("Ohh! shitt!. This game is draw.")
elif cpoint > ppoint:
    print("Game over!!!")
else:
    print("Congratulation!! You won the game.")
print("\n")