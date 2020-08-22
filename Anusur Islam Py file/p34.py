number1 = {1,2,3,4,5,5}
number2 = set([4,5,6])
number2.add(7)
number2.remove(7)

print(number1)
print(7 in number2)
print(4 not in number2)

print()

print( number1 | number2)
print( number1 & number2)
print( number1 - number2)