class Bike:
    def __init__(self,name,color):
        self.name  = name
        self.color = color
    def __eq__(self, other):
        return self.name == other.name and self.color == other.color;
    def __str__(self):
        return (f"Name = {self.name}, Color = {self.color}")
    def diplay(self):
        print(f"Name = {self.name}, Color = {self.color}")

bike1 = Bike("yamaha r15","Blue")
bike2 = Bike("yamaha r15","Blue")

print(bike1==bike2)
print(bike2)