from random import randint

# użycie metody cramera do wyznaczania rozwiązań układu równań o n niewiadomych
# wersja bez funkcji bibliotecznych, nieefektywna o dużej złożoności obliczeniowej

n = 0


# funkcja znajdująca wyznacznik w macierzy
def find_det(array, n):
    det = 0

    # suma z lewej na skos
    k = 0
    while k < n:
        num = 1
        for i in range(0, n):
            num = num * array[(i + k) % n][i]
        det += num
        k += 1

    # suma z prawej na skos
    k = 0
    while k > -n:
        num = 1
        for i in range(0, n):
            num = num * array[((i+1)*(-1) + k) % n][i]
        det -= num
        k -= 1

    return det


# funkcja która podmienia i-tą kolumnę na kolumnę z tablicy wyników równań
def replace(array, column, index):
    new_array = [row[:] for row in array]
    for i in range(0, n):
        new_array[i][index] = column[i]
    return new_array


while n < 2:
    try:
        n = int(input("Podaj liczbę niewiadomych w układzie równań (musi być większa od 1) "))
    except ValueError:
        print("Podano nieprawidłową liczbę. Spróbuj jeszcze raz")

# tablica na współczynniki rzeczywiste przy niewiadomych
W = [[] for _ in range(0, n)]
# tablica na wyniki równań
S = []

# generowanie współczynników całkowitych w macierzy nxn
for i in range(0, n):
    S.append(randint(1, 9))
    for j in range(0, n):
        W[i].append(randint(1, 9))

# wyświetlenie układu równań
print(f"Układ równań z {n} niewiadomymi: ")
for i in range(0, n):
    line = ""
    for j in range(0, n - 1):
        line += str(W[i][j]) + chr(97 + j) + " + "

    line += str(W[i][n - 1]) + chr(97 + n - 1) + " = " + str(S[i])
    print(line)
det_main = find_det(W, n)
print("Wyznacznik główny: ", det_main)

for i in range(0, n):
    letter = chr(97 + i)
    det = find_det(replace(W, S, i), n)
    print(f"Wyznacznik {letter}: ", det)
    print(f"Rozwiązanie {letter} = ", det / det_main)
