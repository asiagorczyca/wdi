# utworzenie tablicy na liczby całkowite podane przez użytkownika
numbers = []
# utworzenie tablicy na liczby podane przez użytkownika i dopełnienia
filled = []

print("Podaj 5 liczb całkowitych i oddziel je enterem: ")

# dodanie 5 liczb całkowitych do tablicy, w przypadku błędu czynność jest poiwtarzana do skutku
while len(numbers) < 5:
    try:
        numbers.append(int(input()))
    except ValueError:
        print("Podano nieprawidłową wartość")

# wypełnienie "dziur" między elementami
for i in range(0, len(numbers) - 1):
    start = numbers[i]
    end = numbers[i + 1]

    """ 
    jeżeli kolejny element jest większy od poprzedniego, 
    to będziemy zwiększać nasze liczby o 1,
    dopóki nie dojdziemy do kolejnego elementu
    w przypadku, gdy element kolejny jest mniejszy od poprzedniego,
    to będziemy zmniejszać nasze liczby o 1,
    dopóki nie dojdziemy do kolejnego elementu
    """
    if start < end:
        step = 1
    else:
        step = -1

    # dodanie do tablicy wynikowej liczb z zakresu od pierwszej włącznie do ostatniej
    # step - o ile zwiększamy/zmniejszamy liczbę
    filled.extend(range(start, end, step))

# dodanie ostatniego elementu, który nie jest dodany podczas wykonywania pętli
filled.append(numbers[-1])

print(filled)
