num = [1,2,3,4,5]

result = [x*x for x in num]
print(result)
print()

result = list( filter( lambda x: x%2==0, num))
print(result)

result= [x for x in num if x%2==0] #list comprehensions
print(result)
print()

result = list(map(lambda x: x*x,num))
print(result)