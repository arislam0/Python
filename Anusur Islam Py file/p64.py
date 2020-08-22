import re
#pattern = r"ice(-)?cream"
pattern = r"a{1,3}$"

if re.match(pattern,"aaaa"):
    print("Matched")
else:
    print("Not Matched")