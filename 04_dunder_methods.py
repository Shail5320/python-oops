# In Python, magic methods (also called dunder methods) are 
# special methods whose names start and end with double underscores.

# python may call themself irrespective of you calling them explicitly

# You define	        You use
# def add()	            z1.add(z2)
# def __add__()	        z1 + z2
# def __sub__() 	    z1 - z2
# def __mul__()	        z1 * z2
# def __truediv__()	    z1 / z2

# len(obj)       → obj.__len__()
# print(obj)     → obj.__str__()
# obj1 == obj2   → obj1.__eq__(obj2)
# obj[i]         → obj.__getitem__(i)

# a + b
#   ↓
# a.__add__(b)
#   ↓
# your implementation
#   ↓
# result

# Operator overloading = giving an existing Python operator a meaning for your own objects
# ie a add or + can add 2 numbers, concatenate 2 strings and extend a list 