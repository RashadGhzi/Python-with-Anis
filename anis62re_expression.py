import re           # (re) means regular expression

#pattern = r"Green"  #1
#pattern = r"green" #2
pattern = r"green"
#a = re.match(pattern,"Green is one of my fovourite colour. Peope love green")  #1
#a = re.search(pattern,"Green is one of my fovourite colour. Peope love green")  #2
a = re.findall(pattern,"green is one of my fovourite colour. Peope love green")
if a:
    print(a)
else:
    print("There is nothing like this.")