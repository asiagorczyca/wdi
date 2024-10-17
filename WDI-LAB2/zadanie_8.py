# zadanie 9

tiers = int(input("Ile pięter ma mieć choinka?: "))

# wersja bez pnia

print("Wersja bez pnia: ")
base = 1

# obliczenie ile gwiazdek będzie znajdowało się na najniższym poziomie choinki
for i in range(1, tiers):
    base += 2

# obliczenie ile spacji bedzie po lewej stronie gwiazki na najwyższym poziomie
empty_spaces = int((base-1)/2)
stars = 1

"""dopóki liczba gwiazdek, zwiększanych o 2 co poziom, nie będzie większa od liczba gwiazdek
 na najniższym poziomie choinki dla podanej liczby pięter, wykonuj wypisanie spacji po lewej 
 stronie od gwiazdek (zmniejszanej o 1 co poziom)"""

while stars<=base:

    print(" "*empty_spaces, "*"*stars, sep="")
    stars+=2
    empty_spaces-=1

print("\nWersja ze szpicem: ")

empty_spaces = int((base-1)/2)


# dodajemy szpic
print(" "*empty_spaces, "X", sep="")
""" najwyższe piętro jest zrobione, więc zmieniamy liczbę spacji po lewej stronie od gwazdek, 
tak aby była odpowiednia dla drugiego piętra oraz liczbę gwiazdek na piętro, aby zacząć od drugiego piętra od góry """

stars = 3
empty_spaces-=1
current_tier = 1 # określenie piętra, które jest obecenie wypisywane

"""
ułożenie bombki na pietrze jest zależne od parzystości piętra,
jeśli piętro jest nieparzyste (zakładając, że szpic jest na pierwszym piętrze, 
a każde kolejne piętro ma numer o jeden większy), to bombka znajduje się o 1 na prawo od środka piętra,
a jeżeli piętro jest parzyste, to bombka znajduje sie na pozycji o jeden większej na lewo od środka piętra
od pozycji na poprzednim piętrze nieparzystym, tzn. dla piętra 2 licząc od góry na pozycji o 1 na lewo od pnia,
na piętrze 4 już na pozycji o 2 na lewo od środka piętra itd. 
"""

pos_left = 0 #pozycja na lewo od środka piętra dla pięter parzystych

while stars<=base:
    current_tier += 1
    if current_tier % 2 == 1:
        half = int(stars/2)+1
        print(" "* empty_spaces, "*"*half, "o", "*"*(stars-half-1), sep="")
    else:
        print(" "* empty_spaces, "*"*pos_left, "o", "*"*(stars-pos_left-1), sep="")
        pos_left+=1
    stars+=2
    empty_spaces-=1

print("\nWersja z pniem: ")

# kod ten sam co poprzednio, mogłby być funkcją
empty_spaces = int((base-1)/2)
stars = 3

print(" "*empty_spaces, "X", sep="")

empty_spaces-=1
current_tier = 1
pos_left = 0

while stars<=base:
    current_tier += 1
    if current_tier % 2 == 1:
        half = int(stars/2)+1
        print(" "* empty_spaces, "*"*half, "o", "*"*(stars-half-1), sep="")
    else:
        print(" "* empty_spaces, "*"*pos_left, "o", "*"*(stars-pos_left-1), sep="")
        pos_left+=1
    stars+=2
    empty_spaces-=1

empty_spaces = int((base-1)/2)

# dodanie pnia na środku ostatniego piętra
print(" "*empty_spaces, "U", sep="")

