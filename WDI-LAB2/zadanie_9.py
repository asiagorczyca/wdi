# zadanie 9

# informacje o użytkowniku

saldo = 3200
pin = '1234'

print("Wybierz operację poprzez podanie odpowiadającego jej numeru: ")

# program zapętla się dopóki uzytkownik go nie zakończy poprzez wybranie odpowiedniej opcji
while True:
    # menu z dostępnymi opcjami
    print("1 - Dokonaj wpłaty",
          "\n2 - Dokonaj wypłaty",
          "\n3 - Pokaż saldo",
          "\n0 - Zakończ działanie programu"
          )
    choice = int(input("Wybrana operacja: "))

    """zinterpretowanie opcji wybranej przez użytkownika jako odpowiednio wpłata, wypłata, 
    pokazanie salda oraz zakończenie działania programu oraz sprawdzenie PINu dla każdej z opcji """

    if choice == 1:
        if input("Podaj PIN: ")==pin:
            amount = int(input("Podaj kwotę kótrą chcesz wpłacić: "))
            # dodanie kwoty podanej przez użytkownika do salda
            saldo = saldo+amount
            print("Kwota została wpłacona")
        else:
            print("Nieprawidłowy numer PIN")
    elif choice == 2:
        if input("Podaj PIN: ")==pin:
            amount = int(input("Podaj kwotę kótrą chcesz wypłacić: "))
            # sprawdzenie, czy kwota podana przez użytkownika może zostać wypłacona
            if(amount<=saldo):
                #wypłacenie kwoty
                saldo = saldo - amount
                print("Kwota została wypłacona")
            else:
                print("Niewystarczające środki na koncie")
        else:
            print("Nieprawidłowy numer PIN")
    elif choice == 3:
        if input("Podaj PIN: ") == pin:
            # pokazanie salda
            print("Saldo:", saldo)
        else:
            print("Nieprawidłowy numer PIN")
    else:
        # zakończenie programu przez użytkownika
        break

    print("Co chcesz zrobić w kolejnym kroku?")






