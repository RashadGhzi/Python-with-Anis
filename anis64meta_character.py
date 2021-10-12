import re   # (re) means regular expression

# 1
"""pattern = r"^col..r$"    # (.) dot means any character. (^) means start and ($) means end.
if re.match(pattern,"colour"):
    print("Mached")
else:
    print("error")"""

# 2
"""pattern = r"a*"             # (*) star means 0 or more. 
if re.search(pattern,"aaaaa"):
    print("match")
else:
    print("error")"""

# 3
"""pattern = r"a+"                # (+) plus means 1 or more.
if re.search(pattern,"aaaaaaasd"):
    print("Matched")
else:
    print("error")
"""

# 4
"""
pattern = r"ice(-)?cream"                # (?) question means 0 or 1.
if re.search(pattern,"ice-cream"):
    print("Matched")
else:
    print("error")
"""


# 5
pattern = r"a{1,3}"                # {1,3}  means 1 or 3.
if re.search(pattern,"aakaffg"):
    print("Matched")
else:
    print("error")
