class Complexnum:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __eq__(self, other):
        if isinstance(other, Complexnum):
            return abs(self.real - other.real) < 1e-9 and abs(self.imag - other.imag) < 1e-9
        return False

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

    @staticmethod
    def solve(a, b, c):
        delta = b.exp(2).subtract(a.multiply(c).multiply(4))
        print("Rozwiązania:")
        if delta.real != 0 or delta.imag != 0:
            x1 = b.multiply(-1).add(delta.find_root()).divide(a.multiply(2))
            x2 = b.multiply(-1).subtract(delta.find_root()).divide(a.multiply(2))
            print(f"x1 = {x1.display()}")
            print(f"x2 = {x2.display()}")
        else:
            x = b.multiply(-1).divide(a.multiply(2))
            print(f"x = {x.display()}")

def main():
    print(Complexnum(1, 0).find_root().display())
    print("Program rozwiązuje równanie kwadratowe ze wspołczynnikami zespolonymi w postaci ax^2+bx+c=0")
    print("Wszystkie współczynniki są w postaci x+yi, gdzie x to część rzeczywista liczby, a y to część urojona")
    print("Współczynnik a: ")
    num1 = Complexnum.input_num()
    print("Współczynnik b: ")
    num2 = Complexnum.input_num()
    print("Współczynnik c: ")
    num3 = Complexnum.input_num()

    Complexnum.solve(num1, num2, num3)
    return 0

if __name__ == '__main__':
    main()