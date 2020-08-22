def calculate(a,b):
    return a*a+2*a*b+b*b
print(calculate(2,3))
#name function
print()

(lambda  a,b: a*a+2*a*b+b*b)(2,3)

print((lambda  a,b: a*a+2*a*b+b*b)(2,3))
print((lambda  a: a*a*a)(2))
