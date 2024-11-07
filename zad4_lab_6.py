from random import randint

n = 0


# funkcja która podmienia i-tą kolumnę na kolumnę z tablicy wyników równań
def replace(array, column, index):
    new_array = [row[:] for row in array]
    for i in range(0, n):
        new_array[i][index] = column[i]
    return new_array


# funkcja do usunięcia pierwszego rzędu i i-tej kolumny w macierzy
def remove(array, column):
    new_array = [row[:] for row in array]
    del (new_array[0])
    for row in new_array:
        del (row[column])
    return new_array


# funkcja do wyliczenia wyznacznika macierzy
def calculate_det(mat, n):
    # przypadek dla macierzy 1x1
    if n == 1:
        return mat[0][0]
    # przypadek dla macierzy 2x2
    if n == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

    det = 0

    for i in range(0, n):
        det += (-1) ** i * mat[0][i] * calculate_det(remove(mat, i), n - 1)

    return det


while n < 1:
    try:
        n = int(input("Podaj liczbę niewiadomych w układzie równań "))
        if n < 1:
            print("Podana liczba musi być większa lub równa 1. Spróbuj jeszcze raz")
    except ValueError:
        print("Podano nieprawidłową liczbę. Spróbuj jeszcze raz")

# tablica na współczynniki rzeczywiste przy niewiadomych
W = [[] for _ in range(0, n)]
# tablica na wyniki równań
S = []

# generowanie współczynników całkowitych w macierzy nxn
for i in range(0, n):
    S.append(randint(-9, 9))
    for j in range(0, n):
        W[i].append(randint(-9, 9))

# przypadki testowe

# dla układu sprzecznego
"""W = [[2, -4, 1],
     [8, -2, 4],
     [-4, 1, -2]]
S = [3, 7, -14]"""

# dla układu, który ma nieskończenie wiele rozwiązań
"""W = [[2, -4, 1],
     [8, -2, 4],
     [-4, 1, -2]]
S = [3, -14, 7]"""

# wyświetlenie układu równań
print(f"Układ równań z {n} niewiadomymi: ")
for i in range(0, n):
    line = ""
    for j in range(0, n - 1):
        line += str(W[i][j]) + chr(97 + j) + " + "

    line += str(W[i][n - 1]) + chr(97 + n - 1) + " = " + str(S[i])
    print(line)
det_main = int(calculate_det(W, n))
print("Wyznacznik główny: ", det_main)

dets = []

for i in range(0, n):
    dets.append(int(calculate_det(replace(W, S, i), n)))

if det_main != 0:
    for i in range(0, n):
        letter = chr(97 + i)
        print(f"Wyznacznik {letter}: ", dets[i])
        print(f"Rozwiązanie {letter} = ", dets[i] / det_main)
elif det_main == 0 and set(dets) != {0}:
    print("Układ jest sprzeczny")
else:
    print("Układ ma nieskończenie wiele rozwiązań")
