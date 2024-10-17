# zadanie 7
print("zadanie 7: ")
# program wykorzystuje pętle while i for

# podanie przez użytkownika zakresu liczb

start = int(input("Podaj początek zakresu: "))
end = int(input("Podaj koniec zakresu: "))

# obliczenie ile liczb jest w zakresie
len = end-start+1

sum=0
# obliczenie sumy wszystkich liczb w zakresie

for i in range(start, end+1):
    sum=sum+i

# obliczenie średniej liczb w zakresie

avg = int(sum/len)

"""jeśli liczba elementów w zakresie nie jest większa od 20,
 to program wypisze wszystkie liczby z zakresu,
 w przeciwnym wypadku, program wypisze 6 liczb najbliższych
 średniej tych liczb, ale z pominięciem sredniej"""
if len<=20:
    while start<end+1:
        print(start)
        start+=1
else:
    for i in range(avg-3, avg):
        print(i)
    for i in range(avg+1, avg+4):
        print(i)

