class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Creating instances
num1 = ComplexNumber(2, 3)
num2 = ComplexNumber(1, 2)

# Performing operations
sum_result = num1 + num2
mul_result = num1 * num2

# Printing results
print("Sum:", sum_result)
print("Product:", mul_result)
