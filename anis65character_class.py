import re

pattern = r"[A-B][a-b][0-9]"

if re.match(pattern,"Xc8"):
    print("matched")
else:
    print("error")