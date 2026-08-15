class Pen():
    def __init__ (self, brand, color, type, price):
        self.brand = brand
        self.color = color
        self.type = type
        self.price = price

    def info(self):
        print(f"The Brand Name for the pen is {self.brand}")
        print(f"The ink color for the pen is {self.color}")
        print(f"The type for the pen is {self.type}")
        print(f"The cost for the pen is {self.price}")

    def pen_cost(self, qty):
        return qty*self.price


p1 = Pen("uniball", "Red", "Roller Ball", 65)
p2 = Pen("Luxor", "Black", "Fountain", 90)
p3 = Pen("Flair", "Blue", "Gel", 20)

print(Pen.pen_cost(p1, 10))
Pen.info(p2)
