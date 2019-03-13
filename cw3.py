#zadanie 1 (caa.py)
krotka = ("a", "B", 12, "python", 27, [2,4])
print(krotka)
#Nie da się zmienić elemetu w krotce
print(krotka[3])
print(krotka[-5])

#zadanie 2 (cab.py)
zbior = set(["Inżynieria", "Systemów", "Informatycznych"])
print(zbior)
zbior.add("Systemów")
print(zbior)
#W zbiorze nie może być więcej niż jeden dany element a w tym już istnieje element "Systemów"

#Nie da się wykonać poleceń z zadania 1, ponieważ zbiory nie wspierają indeksowania elementów


#zadanie 3 (cac.py)

slownik = {"Jan" : 533125664, "Anna" : 677309231, "Adam" : 789979684}
for "Jan", 533125664 in slownik:
 print("&s ma numer telefonu &d" % ("Jan", 533125664))
del(slownik["Jan"])
print(slownik)

#zadanie 4 (cad.py)

liczba = input("Podaj cyfre rzymską od 1 do 100 ")
def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    return -1

def rzymskanaarab(str):
    res = 0
    i = 0
    while (i < len(str)):
        s1 = value(str[i])
        if (i + 1 < len(str)):
            s2 = value(str[i + 1])
            if (s1 >= s2):
                res = res + s1
                i = i + 1
            else:
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
    return res

print("Podana liczba rzymska to:  "),
print(rzymskanaarab(liczba))

#zadanie 5 (cae.py)

l=input("Podaj ciąg!\n")
print(l)
for wart in l:
   pisemnie=('0','1','2','3','4','5','6','7','8','9')
   if wart in pisemnie:
       slownie={0:'Zero',1:'Jeden',2:'Dwa',3:'Trzy',4:'Cztery',5:'Pięć',6:'Sześć',7:'Siedem',8:'Osiem',9:'Dziewięć'}
       print(slownie[int(wart)])

#zadanie 6 (caf.py)

zbior1 = set(['Warszawa', 'Poznań', 'Olsztyn', 'Łódź', 'Kraków'])
zbior2 = set(['Katowice', 'Poznań', 'Gdańsk', 'Kielce'])
zbior3 = set(['Warszawa', 'Olsztyn', 'Szczecin', 'Białystok', 'Lublin', 'Poznań'])

zbior4 = zbior1.union(zbior2, zbior3)
print(zbior4)
zbior5 = zbior1.intersection(zbior2, zbior3)
print(zbior5)
zbior6 = zbior1.difference(zbior2)
print(zbior6)

#zadanie 7 (cag.py)

PESEL = input("Podaj PESEL: \n")
if len(PESEL) < 11:
    print('Niepoprawny PESEL')

if len(PESEL) > 11:
    print ('Niepoprawny PESEL')
print(PESEL)