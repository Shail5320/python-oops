class ComplexNumbers:
    def __init__(self, real = 0.0, imag = 0.0):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.real==0:
            return f"{self.imag}"
        elif self.imag < 0:
            return f"{self.real}{self.imag}"
        else:
            return f"{self.real}+{self.imag}"   

    def __add__(self, other):
        return ComplexNumbers(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumbers(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return ComplexNumbers(self.real * other.real - self.imag * other.imag, self.real * other.imag + other.real * self.imag)

    def __truediv__(self, other):
        den = other.real**2 + other.imag**2
        return self * ComplexNumbers(other.real/den,(-1*other.imag)/den)

    def conjugate(self):
        return ComplexNumbers(self.real, -1*self.imag)