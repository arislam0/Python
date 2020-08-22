file = open("student","r+")
"""
text = file.read()
print(text)
size = len(text)
print(size)

"""
print()
#text1=file.readlines()[3]
#text1=file.readlines()

for line in file:
    print(line)

"""
print()
print(file.readable())
print(file.writable())
"""

file.close()