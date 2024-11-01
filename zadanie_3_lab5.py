import itertools

#
sets = []
input_copy = []


def generate_alternatives(digits, results_number):
    for i in range(0, results_number):
        permutations = list(set(int("".join(p)) for p in itertools.permutations(digits)))[:results_number]
        return permutations


print("Podaj trzy liczby całkowite i oddziel je enterem")
while len(sets) < 3:
    try:
        current = str(int(input()))
        input_copy.append(current)
        sets.append(set(current))
    except ValueError:
        print("Podano nieprawidłowe dane, spróbuj jeszcze raz")

if sets[0] == sets[1] == sets[2]:
    print("Trzy podane liczby są zbudowane z tych samych cyfr")
else:
    print(
        "Podane liczby nie są zbudowane z tych samych cyfr. \nAlternatywne liczby wejściowe, które dałyby wynik pozywtywny dla każdej z podanych liczb: ")

    for i in range(0, len(input_copy)):
        current = input_copy[i]
        print(f"Dla {current}: {generate_alternatives(current, 3)}")
