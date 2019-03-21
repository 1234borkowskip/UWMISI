def silnia(a):
    wynik = 1
    while a > 0:
        wynik = a * wynik
        a = a - 1
    return wynik


print(silnia(3))
print(silnia(10))
print(silnia(5))