"""
Zadanie 4.
Napisać program rozwiązujący równanie
x^2-2=0
 metodą bisekcji.
"""


# funkcja sprawdza, czy dla danego x wartość funkcji f(x) jest dodatnia (prawda), czy ujemna (fałsz)
def isPositive(x):
    if x ** 2 - 2 > 0:
        return 1
    else:
        return 0


# znalezienie liczb a i b takich, że f(a)<0 i f(b)>0

a = 0
b = 0

while not isPositive(b):
    b += 1

# obliczenie średniej liczb a i b

avg = float(a + b) / 2.0

while abs(round(avg ** 2 - 2, 8)) > 0.0000001:
    if isPositive(avg):
        b = avg
    else:
        a = avg
    avg = float(a + b) / 2.0

""" 
wiadomo, że dla wielomianu x^2-2=0 odległość jednego rozwiązania od osi y jest taka 
sama jak odległośc drugiego rozwiązania od osi y,
więc drugie rozwiązanie jest liczbą przeciwną do pierwszego rozwiązania

"""
avg = round(avg, 8)
print(f"Rozwiązania równania x^2-2=0: \nx1={avg}\nx2={-avg}")
