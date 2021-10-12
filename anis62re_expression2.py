import re              # (re) means regular expression

pattern = r"love"
a = re.search(pattern,"I love my garden.")
if a:
    print(a.start())
    print(a.end())
    print(a.span())
else:
    print("error")