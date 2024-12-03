def find_primes(n, numbers, i):
    if i <= n ** (1 / 2):
        numbers = [x for x in numbers if x % i != 0 or x == i]
        return find_primes(n, numbers, i + 1)
    return numbers


n = int(input("Podaj liczbę n, dla której szukamy liczb rzeczywistych mniejszych od niej lub jej równych: "))
numbers = list(range(2, n + 1))
print(f"Liczby pierwsze mniejsze lub równe {n}:\n {find_primes(n, numbers, 2)}")
