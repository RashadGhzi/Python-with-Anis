import re           # (re) means regular expression

pattern = r"colour"
text = "Everyone like red colour. Red  is one of the best colour."
text2 = re.sub(pattern,"color",text,count=2)
text3 = re.search(pattern,text)
print(text2)
if text3:
    print("match")
else:
    print("error")