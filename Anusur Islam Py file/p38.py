#xargs
def student(*details):
    print(details)
student(101,"Ar")
student(101,"Ar",3.75)
print()

def add(*numbers):
   sum = 0
   for num in numbers:
       sum = sum + num
   print(sum)

add(10,20)
add(10,20,30)
add(10,20,30,40)
print()

def student1(**details):
    print(details)
    print(details["name"])

student1(id=101,name="anis")
print()