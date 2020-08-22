"""
import  re
pattern = r"colour"
if(re.match(pattern,"colour is a colour, I love red colour")):
    print("Match")
else:
    print("Not Matched")

if(re.search(pattern,"Red is a colour, I love red colour")):
    print("Match")
else:
    print("Not Matched")

print()

print(re.findall(pattern,"Red is a colour, I love red colour"))

print()
"""
import  re
pattern = r"colour"
text = "My favourite colour is Red."
match = re.search(pattern,text)

if(match):
    print(match.start())
    print(match.end())
    print(match.span())