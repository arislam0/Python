class Student:
    roll=""
    gpa=""
    def setValue(self,roll,gpa):
        self.roll=roll
        self.gpa =gpa
    def display(self):
         print(f"Roll: {self.roll},GPA: {self.gpa}")


rahim = Student()
#print(isinstance(rahim,Student))
rahim.setValue(101,3.75)
rahim.display()

karim = Student()
#print(isinstance(rahim,Student))
karim.setValue(102,3.56)
karim.display()