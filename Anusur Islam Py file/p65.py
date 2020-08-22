import  re
#pattern =  r"[aeiou]"
#pattern =  r"[A-Z]"
pattern =  r"[0-9]"
pattern =  r"[A-Z][a-z][0-9]"

if re.match(pattern,"Aa0gggg"):
    print("Matched")
else:
    print("Not matched")