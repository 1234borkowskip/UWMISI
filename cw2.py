import math

# zadanie 2
print(math.ceil(5.67))
print(math.ceil(45.34 - 6))
print(math.floor(5.67))
print(math.floor(22))
print(math.floor(-4.78))
print(math.factorial(6))
print(math.factorial(1))
print(math.factorial(0))
print(math.gcd(1024,144))
print(math.fabs(-15))
print(math.exp(3))
print(math.log(12))
print(math.log10(25))
print(math.log(6,4))
print(math.pow(5,6))
print(math.sqrt(34))
print(math.pi + 6)
print(math.cos(3))
print(math.sin(2 * math.pi))
#zadanie 3
str = "programowaniestrukturalne"
print(str)
print(str[::2])
print(str[22:25])
print(str[12])
print(2 * str)
#zadanie 4
napis = input("Podaj napis ")
wspak = napis[::-1]
print(wspak)
#zadanie 5
napis1 = input("Podaj 1 słowo ")
napis2 = input("Podaj 2 słowo ")
napis3 = input("Podaj 3 słowo ")
napis4 = input("Podaj 4 słowo ")
napis5 = input("Podaj 5 słowo ")
print(len(napis1))
print(len(napis2))
print(len(napis3))
print(len(napis4))
print(len(napis5))
#zadanie 6 i 7
lista = ['kawa', 'mleko', 'jajka', 'chleb', 'chleb', 'cola', 'kawa']
print(lista)
print("chleb =", lista.count('chleb'))
print("herbata =",lista.count('herbata'))
print("cola index =",lista.index("cola"))
print(set(lista))
znaki = input("Podaj słowo ")
print("W twoim wyrazie mała litera a występuje", znaki.count("a"),"razy")
# zadanie 9
wiek = 19
dwa = 2
trzy = 3
imie = "Paweł"
nazwisko = "Borkowski"
print("Witam, nazywam się %s %s" % (imie, nazwisko))
print("Mam %s lat" %wiek)
print("Witaj {imie} {nazwisko}. Ma Pan {wiek} lat.".format(imie=imie, nazwisko=nazwisko, wiek=wiek))
print("%s + %s =" %(dwa, trzy) , dwa + trzy)
print("{dwa} + {trzy} = 5".format(dwa=dwa, trzy=trzy))

# zadanie 10
miesiace = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'lipiec', 'sierpień', 'październik', 'listopad', 'grudzień']
miesiace.sort()
print("miesiące alfabetycznie", miesiace)
#zadanie 11
nazwisko1 = input("Podaj nazwisko ")
nazwisko2 = input("Podaj nazwisko ")
nazwisko3 = input("Podaj nazwisko ")
nazwisko4 = input("Podaj nazwisko ")
nazwisko5 = input("Podaj nazwisko ")
tablica = [nazwisko1, nazwisko2, nazwisko3, nazwisko4, nazwisko5]
print("Nazwiska zaczynające się od liter późniejszych w alfabecie niż P: ")
for x in range(5):
    if 'P' <= tablica[x][0] <= 'Z':
        print(tablica[x])
print("Nazwiska dłuższe niż 6 znaków: ")
for x in range(5):
    if 6 < len(tablica[x]):
        print(tablica[x])