def sredniawieku(**kwargs):
    suma = 0
    for key, value in kwargs.items():
        suma = suma + value
    return suma/len(kwargs)


print("Srednia wieku: ", sredniawieku(Kamil=1, Krzysztof=2, Mati=3, Barti=4, Pawel=5))
print("Srednia wieku: ", sredniawieku(Kamil=3, Krzysztof=23, Mati=34, Barti=13, Pawel=100))
