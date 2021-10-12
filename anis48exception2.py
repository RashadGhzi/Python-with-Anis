def vote (n):
    if n < 18:
        raise ValueError("You are not allowed.")
    return ("You are allowed to vote.")
try:
    print(vote(20))
except ValueError as e:
    print(e)