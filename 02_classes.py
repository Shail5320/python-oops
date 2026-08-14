# a class is a blueprint
# an object is an instance of a class

class Laptop:
    pass

HP = Laptop()
print(type(HP))

# it has a type <class '__main__.Laptop'>

# python gives us 'object literal' for built in data types

# class comprises of data/attributes/property and methods

# In Python, a constructor is a special method that is automatically called when you create an object from a class.

class Pen():
    def __init__ (self, brand, color, type):
        self.brand = brand
        self.color = color
        self.type = type

p1 = Pen("uniball", "Red", "Roller Ball")
print(type(p1))