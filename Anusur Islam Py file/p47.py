"""
num2 = int( input("Enter a number: ") )
result = 20 / num2
print(result)
print("Done")

except IndexError:
    print("Index error")
"""
try:
    list = [20,0,30]
    result = list[0] / list[3]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Dividing by zero is not possible")


finally:
       print("Successful")
