def czy_sortowanko(lista):
    for x in range(1,len(lista)-1):
        if lista[x-1] < lista[x]:
            return False
    return True


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Lista 1: ",lista)
if czy_sortowanko(lista) is True:
    print("Lista 1 jest posortowana malejąco")
else:
    print("Lista 1 nie jest posortowana malejąco")

lista2 = [10, 9, 8, 7, 6, 5]

print("Lista 2: ",lista2)
if czy_sortowanko(lista2) is True:
    print("Lista 2 jest posortowana malejąco")
else:
    print("Lista 2 nie jest posortowana malejąco")
