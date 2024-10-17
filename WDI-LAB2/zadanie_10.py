import random

while True:
    print("Podaj liczby, na których chcesz wybrane działanie, a następnie wybierz operację, którą chcesz wykonać")
    print("Lista operacji:")
    print("+ - dodawanie",
          "\n- - odejmowanie",
          "\n* - mnożenie",
          "\n/ - dzielenie",
          "\n^ - potęgowanie",
          "\n# - pierwiastkowanie"
          "\nx - losowanie liczby z zakresu")
    a=int(input())
    b=int(input())
    choice = str(input())

    if choice == "+":
        print("wynik operacji: ", a+b)
    elif choice == "-":
        print("wynik operacji: ", a-b)
    elif choice == "*":
        print("wynik operacji: ", a*b)
    elif choice == "/":
        print("wynik operacji: ", a/b)
    elif choice == "^":
        print("wynik operacji: ", a**b)
    elif choice == "#":
        print("wynik operacji: ", a**(1/b))
    else:
        if a<=b:
            print("wynik operacji: ", random.randint(a,b))
        else:
            print("wynik operacji: ", random.randint(b, a))


    next=input("Czy chcesz wprowadzić nowe dane? (T/N) ")
    if next.capitalize() == "N":
        break



