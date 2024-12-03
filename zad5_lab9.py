class Complexnum:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag


def display(num):
    if num.real != 0 and num.imag != 0:
        return f"{num.real} + {num.imag}i"
    elif num.real == 0 and num.imag != 0:
        return f"{num.imag}i"
    elif num.real != 0 and num.imag == 0:
        return f"{num.real}"
    else:
        return "0"


def num_input():
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


def add(num1, num2):
    result = Complexnum(num1.real + num2.real, num1.imag + num2.imag)
    return result


def subtract(num1, num2):
    result = Complexnum(num1.real - num2.real, num1.imag - num2.imag)
    return result


def multiply(num1, num2):
    result = Complexnum(num1.real * num2.real - num1.imag * num2.imag, num1.real * num2.imag + num2.real * num1.imag)
    return result


def divide(num1, num2):
    return Complexnum((num1.real * num2.real + num1.imag * num2.imag) / (num2.real ** 2 + num2.imag ** 2),
                      (num1.imag * num2.real - num1.real * num2.imag) / (num2.real ** 2 + num2.imag ** 2))


def exp(num, power):
    if power == 0:
        return 1
    if power == 1:
        return num
    return multiply(exp(num, power - 1), num)


def find_root(num):
    a = num.real
    b = num.imag

    x = abs(((a + (a * a + b * b) ** (1 / 2)) / 2) ** (1 / 2))
    if x != 0:
        y = b / (2 * x)
    else:
        y = (-a) ** (1 / 2)

    return Complexnum(x, y)


def solve(a, b, c):
    delta = subtract(exp(b, 2), multiply(multiply(a, c), 4))
    print("Rozwiązania:")
    if delta.real != 0 or delta.imag != 0:
        x1 = divide(add(multiply(b, -1), find_root(delta)), multiply(a, 2))
        x2 = divide(subtract(multiply(b, -1), find_root(delta)), multiply(a, 2))
        print(f"x1 = {display(x1)}")
        print(f"x2 = {display(x2)}")
    else:
        x = divide(multiply(b, -1), multiply(a, 2))
        print(f"x = {display(x)}")

print("Program rozwiązuje równanie kwadratowe ze wspołczynnikami zespolonymi w postaci ax^2+bx+c=0")
print("Wszystkie współczynniki są w postaci x+yi, gdzie x to część rzeczywista liczby, a y to część urojona")
print("Współczynnik a: ")
num1 = num_input()
print("Współczynnik b: ")
num2 = num_input()
print("Współczynnik c: ")
num3 = num_input()

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




