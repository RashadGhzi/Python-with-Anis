
from  random import randint
a = 1
while a < 6:
    print("Enter your guess number between 1 to 5:")
    guessnum = int(input())
    randomnum = randint(1,5)
    if guessnum == randomnum:
        print("You have won the game.")
        break
    else:
        print("You have lose the game.")
    print("Random number was ", randomnum)
    a = a + 1