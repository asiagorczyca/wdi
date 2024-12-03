class Complexnum:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def display(self):
        if self.real != 0 and self.imag != 0:
            return f"{self.real} + {self.imag}i"
        elif self.real == 0 and self.imag != 0:
            return f"{self.imag}i"
        elif self.real != 0 and self.imag == 0:
            return f"{self.real}"
        else:
            return "0"

    def add(self, other):
        return Complexnum(self.real + other.real, self.imag + other.imag)

    def subtract(self, other):
        return Complexnum(self.real - other.real, self.imag - other.imag)

    def multiply(self, other):
        return Complexnum(self.real * other.real - self.imag * other.imag,
                          self.real * other.imag + other.real * self.imag)

    def divide(self, other):
        return Complexnum((self.real * other.real + self.imag * other.imag) / (other.real ** 2 + other.imag ** 2),
                          (self.imag * other.real - self.real * other.imag) / (other.real ** 2 + other.imag ** 2))

    def exp(self, power):
        if power == 0:
            return 1
        if power == 1:
            return self
        return self.multiply(self.exp(power - 1))

    def find_root(self):
        x = abs(((self.real + (self.real ** 2 + self.imag ** 2) ** (1 / 2)) / 2) ** (1 / 2))
        if x != 0:
            y = self.imag / (2 * x)
        else:
            y = (-self.real) ** (1 / 2)
        return Complexnum(x, y)

    @staticmethod
    def input_num():
        while True:
            try:
                real = float(input("Wprowadź część rzeczywistą liczby: "))
                break
            except ValueError:
                print("Wprowadzona liczba jest nieprawidłowa. Spróbuj jeszcze raz")

        while True:
            try:
                imag = float(input("Wprowadź część urojoną liczby: "))
                break
            except ValueError:
                print("Wprowadzona liczba jest nieprawidłowa. Spróbuj jeszcze raz")

        return Complexnum(real, imag)


def solve(a, b, c):
    delta = Complexnum.subtract(Complexnum.exp(b, 2),
                                    Complexnum.multiply(Complexnum.multiply(a, c), 4))
    print("Rozwiązania:")
    if delta.real != 0 or delta.imag != 0:
        x1 = Complexnum.divide(Complexnum.add(Complexnum.multiply(b, -1), Complexnum.find_root(delta)),
                                   Complexnum.multiply(a, 2))
        x2 = Complexnum.divide(
            Complexnum.subtract(Complexnum.multiply(b, -1), Complexnum.find_root(delta)),
            Complexnum.multiply(a, 2))
        print(f"x1 = {x1.display()}")
        print(f"x2 = {x2.display()}")
    else:
        x = Complexnum.divide(Complexnum.multiply(b, -1), Complexnum.multiply(a, 2))
        print(f"x = {x.display()}")


print("Program rozwiązuje równanie kwadratowe ze wspołczynnikami zespolonymi w postaci ax^2+bx+c=0")
print("Wszystkie współczynniki są w postaci x+yi, gdzie x to część rzeczywista liczby, a y to część urojona")
print("Współczynnik a: ")
num1 = Complexnum.input_num()
print("Współczynnik b: ")
num2 = Complexnum.input_num()
print("Współczynnik c: ")
num3 = Complexnum.input_num()

solve(num1, num2, num3)

# Testy funkcji solve

# Delta = 0 i brak części urojonej
# x^2 + 2x + 1 = 0
# a = 1 + 0i
# b = 2 + 0i
# c = 1 + 0i

# część urojona
# (3i)x^2 + (4i)x + 1i = 0
# a = 0 + 3i
# b = 0 + 4i
# c = 0 + 1i

# część urojona i rzeczywista
# (1+2i)x^2 + (2+3i)x + (1+1i) = 0
# a = 1 + 2i
# b = 2 + 3i
# c = 1 + 1i

# część rzeczywista, urojona i delta = 0
# x^2 + (2i)x - 1 = 0
# a = 1 + 0i
# b = 0 + 2i
# c = -1 + 0i

# delta < 0 i wspołczynniki rzeczywiste
# x^2 + 2x + 5 = 0
# a = 1 + 0i
# b = 2 + 0i
# c = 5 + 0i
