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

# what and why self ?
# self refers to the current object.

# Suppose we have two students:

p2 = Pen("Luxor", "Black", "Fountain")
p3 = Pen("Flair", "Blue", "Gel")

# Both objects use the same class, but they need to store
#  different data.
# self tells Python which object's data you're talking about.

# we use self by convention, you can use other names as well
# the object and the self keyword share the same id in memory

# self is the reference created to the object in a class

# Function vs Method
# A function is a reusable block of code. 
# A method is a function that belongs to an object/class.