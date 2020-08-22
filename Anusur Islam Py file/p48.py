"""
try:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    result = num1/num2
    print(result)
except (ValueError,ZeroDivisionError):
    print("You have entered incorrect input.")

finally:
    print("Thanks !!!")
print()
"""

def voter(age):
    if age<18:
         raise ValueError("Invalid Voter")
    return "You are allowed to vote"

try:
   # print(voter(19))
    print(voter(17))
except ValueError as e:
    print(e)

