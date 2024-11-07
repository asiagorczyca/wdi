from random import randint

n = 0


# funkcja która podmienia i-tą kolumnę na kolumnę z tablicy wyników równań
# replace this function with a function from numpy lib
def replace(array, column, index):
    new_array = [row[:] for row in array]
    for i in range(0, n):
        new_array[i][index] = column[i]
    return new_array


# Function for finding the determinant of a matrix.
def det(mat, n):
    # Base case for 2x2 matrix
    if n == 2:
        return mat[0][0] * mat[1][1] - \
            mat[0][1] * mat[1][0]

    # Recursive case for larger matrices
    res = 0
    for col in range(n):

        # Create a submatrix by removing the first
        # row and the current column
        sub = [[0] * (n - 1) for _ in range(n - 1)]
        for i in range(1, n):
            subcol = 0
            for j in range(n):

                # Skip the current column
                if j == col:
                    continue

                # Fill the submatrix
                sub[i - 1][subcol] = mat[i][j]
                subcol += 1

        # Cofactor expansion
        sign = 1 if col % 2 == 0 else -1
        res += sign * mat[0][col] * det(sub, n - 1)

    return res


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
det_main = int(det(W, n))
print("Wyznacznik główny: ", det_main)

dets = []

for i in range(0, n):
    # dets.append(int(np.linalg.det(replace(W, S, i))))
    dets.append(int(det(replace(W, S, i), n)))

if det_main != 0:
    for i in range(0, n):
        letter = chr(97 + i)
        print(f"Wyznacznik {letter}: ", dets[i])
        print(f"Rozwiązanie {letter} = ", dets[i] / det_main)
elif det_main == 0 and set(dets) != {0}:
    print("Układ jest sprzeczny")
else:
    print("Układ ma nieskończenie wiele rozwiązań")
