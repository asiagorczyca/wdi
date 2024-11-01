import itertools

# stworzenie tablicy, w której znajdują się całe liczby wprowadzone przez uzytkownika
nums = []


# funkcja do sprawdzania, czy wszystkie cyfry każdej liczby są takie same
# first - zbór cyfr pierwszej z liczb
def is_the_same(first, numbers):
    the_same = True
    for number in numbers:
        if set(list(number)) != first:
            the_same = False
    return the_same


# funkcja generuje propozycje liczb złożonych z takich samych cyfr jak wporadzona przez uzytkownika liczba
def generate_alt_nums(number, num_of_alts):
    # minimalny rozmiar liczby to 3, bo muszą być 3 różne liczby
    size = max(len(number), 3)
    # cyfry, które mogą zostac użyte w liczbie
    digits = set(list(number))
    # lista alternatywnych liczb
    alts = []

    # sprawdzenie, czy kombinacja 3 cyfr z liczby nie jest tą samą liczbą i czy składa się ze wszystkich cyfr liczby wejściowej
    # jeśli nie - jest to jedna z alternatyw
    for combination in itertools.product(number, repeat=size):
        new_alt = "".join(combination)
        if set(combination) == digits and new_alt != number:
           alts.append(new_alt)

    # ograniczenie liczby alternatyw do podanej liczby
    alts = alts[:num_of_alts]
    return alts


print("Podaj trzy liczby i oddziel je enterem: ")

# użytkownik wprowadza liczby, dopóki nie będą istnieć 3 zestawy cyfr dla 3 liczb
# w przypadku podania nieprawidłowych danych, musi wprowadzić je jeszcze raz
while len(nums) < 3:
    try:
        number = str(int(input()))
        nums.append(number)
    except ValueError:
        print("Podano nieprawidłowe dane. Spróbuj jeszcze raz")

if is_the_same(set(list(nums[0])), nums):
    print("Podane liczby składają się z tych samych cyfr")
else:
    print("Podane liczby nie składają się z tych samych cyfr. \nAlternatywne opcje:")
    for number in nums:
        print(f"- Dla {number}: ")
        for alt in generate_alt_nums(number, 3):
            print(f"\t-{alt}")
