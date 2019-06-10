import math
'''zadanie 1
class Pracownik:
    def __init__(self, imie, nazwisko, staz):
        self.imie = imie
        self.nazwisko = nazwisko
        self.staz = staz
    def wypisywanie(self):
        print("* ", self.imie, "* ", self.nazwisko, "* ", self.staz, "* ", 3000 +(self.staz*345), "* ")
p1 = Pracownik("Janusz", "Polak", 12)
p1.wypisywanie()'''

'''zadanie 2a
x=int(input("Podaj liczbę dziesiętną "))
print(bin(x)[2:])

zadanie 2b
x = int(input())
print(int(x, 2))'''

'''zadanie 3
def największa(x):
    x.sort()
    print(x[-1])
    x.pop(-1)
    print(x)
x = [2,1,4,6,3,145]
największa(x)

def rekurencja(n):
    if n == 1:
        return 1
    else:
        return rekurencja(n-1)+n
print(" n", "    suma\n", 10,"  ",rekurencja(10))
print(" n", "    suma\n", 2,"   ",rekurencja(2))'''
lista_a=[1,2,3,4,5]
lista_b=[1,2,3,4,5]

mnożenie= [(a * b) for a in lista_a for b in lista_b if a != b]

print(mnożenie)