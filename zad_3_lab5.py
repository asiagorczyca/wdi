import itertools
# add a case if the digit is a zero 
# stworzenie tablicy, w której znajdują się całe liczby wprowadzone przez uzytkownika
nums = []


# funkcja do sprawdzania, czy wszystkie cyfry każdej liczby są takie same
# first - zbór cyfr pierwszej z liczb
def is_the_same(first, numbers):
    return all(set(number) == first for number in numbers)


# funkcja generuje propozycje liczb złożonych z takich samych cyfr jak wporadzona przez uzytkownika liczba
def generate_alt_nums(number, num_of_alts):
    # cyfry, które mogą zostac użyte w liczbie
    digits = set(number)
    # liczba unikalnych cyfr
    size = len(digits)
    # lista alternatywnych liczb
    alts = []

    if size > 1:

        size = max(size, 3)
        # sprawdzenie, czy kombinacja 3 cyfr z liczby nie jest tą samą liczbą i czy składa się ze wszystkich cyfr liczby wejściowej
        # jeśli nie - jest to jedna z alternatyw
        for combination in itertools.product(number, repeat=size):
            new_alt = "".join(combination)
            if set(combination) == digits and new_alt != number and new_alt not in alts:
                alts.append(new_alt)
            if len(alts) == num_of_alts:
                break

        return alts

    return [list(digits)[0] * (len(number) + i) for i in range(1, num_of_alts + 1)]


print("Podaj trzy liczby i oddziel je enterem: ")

# użytkownik wprowadza liczby, dopóki nie będą istnieć 3 zestawy cyfr dla 3 liczb
# w przypadku podania nieprawidłowych danych, musi wprowadzić je jeszcze raz
while len(nums) < 3:
    try:
        number = str(int(input()))
        nums.append(number)
    except ValueError:
        print("Podano nieprawidłowe dane. Spróbuj jeszcze raz")

if is_the_same(set(nums[0]), nums):
    print("Podane liczby składają się z tych samych cyfr")
else:
    print("Podane liczby nie składają się z tych samych cyfr. \nAlternatywne opcje:")
    for number in nums:
        print(f"- Dla {number}: ")
        for alt in generate_alt_nums(number, 3):
            print(f"\t▪ {alt}")
