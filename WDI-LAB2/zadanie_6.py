
# zadanie 6
"""
Program pobiera od użytkownika dwie liczby, a następnie wykonuje na nich operacje:
1) dodawania
2) odejmowania
3) mnożenia
4) dzielenia
oraz wypisuje kwadrat oraz pierwiastek drugiego stopnie obu tych liczb

"""

print("zadanie 6: ")

# pobranie liczb od uzytkownika

a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

# sprawdzenie, czy obie liczby są ujemne, jeśli tak, program nie wykonuje operacj na tych liczbach
if (a<0 and b<0):
    print("Nie można wykonać operacji, ponieważ obie liczby są ujemne")
else:
    if (a<0):
        a=abs(a)
    if(b<0):
        b=abs(b)
    # wykonanie na nich operacji
    print("Suma tych liczb: ", a+b)
    print("Różnica tych liczb: ", a-b)
    print("Iloczyn tych liczb: ", a*b)
    if(a*b==10):
        print("Yay!")
    print("Iloraz tych liczb: ", a/b)
    print("Kwadrat pierwszej liczby: ", a**2)
    print("Kwadrat drugiej liczby: ", b**2)
    print("Pierwiastek kwadratowy pierwszej liczby: ", a**0.5)
    print("Pierwiastek kwadratowy drugiej liczby: ", b**0.5)