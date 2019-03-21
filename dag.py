def sumaKwadratow(*argumenty):
    suma = 0
    for x in range (len(argumenty)):
        suma = suma + argumenty[x] * argumenty[x]
    return suma


print("Pierwszy przypadek testowy:", sumaKwadratow(1, 2, 3, 4, 5))
print("Drugi przypadek testowy:", sumaKwadratow(10, 20, 5))
