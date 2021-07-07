
numberofletter = 0
numberofdigits = 0
numberofwords = 0
text = input("Enter the text of numbers: \n")
for x in text:
    x = x.lower()
    if x >= 'a' and x <= 'z':
        numberofletter = numberofletter + 1
    elif x >= '0' and x <= '9':
        numberofdigits = numberofdigits + 1
    elif x == ' ':
        numberofwords = numberofwords + 1
print(numberofletter)
print(numberofdigits)
print(numberofwords)