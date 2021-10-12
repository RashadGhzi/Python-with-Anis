
from  random import randint
a = 1
try:
    while a < 6:
        print("Enter your guess number between 1 to 5:")
        guessnum = int(input())
        if (guessnum > 5) | (guessnum <= 0):
            print("Enter a correct number.")
            continue
        randomnum = randint(1,5)
        if guessnum == randomnum:
            print("You have won the game.")
            break
        else:
            print("You have lose the game.")
        print("Random number was ", randomnum)
        a = a + 1
except Exception:
    print("Enter a valid keyword")