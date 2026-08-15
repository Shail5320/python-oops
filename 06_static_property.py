# Instance variables are variables that belong to a specific object (instance) of a class. Each object has its own copy of these variables, 
# so changing an instance variable in one object does not affect another object.

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

print(car1.brand)
print(car2.brand)