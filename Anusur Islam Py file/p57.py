"""
class A:
    def displa1(self):
        print("I am inside A class")

class B(A):
    def displa2(self):
        super().displa1()
        print("I am inside B class")

class C(B):
    def displa3(self):
        super().displa2()
        print("I am inside C class")

ob1 = C()
ob1.displa3()
"""

class A:
    def display(self):
        print("I am inside A class")

class B():
    def display(self):
        print("I am inside B class")

class C(B,A):
         pass

ob1 = C()
ob1.display()