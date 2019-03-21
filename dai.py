def trzeciaPotega(*liczby):
    wynik = [liczby[x]*liczby[x]*liczby[x] for x in range(len(liczby))]
    return wynik


print(trzeciaPotega(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(trzeciaPotega(30, 0, 3, 23, -4, 2))
