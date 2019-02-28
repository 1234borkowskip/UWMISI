import math
#zadanie 1
print("Witaj świecie!")

#zadanie 3
a = 5
b = 6
a + b

#zadanie 4
a = 5
b = 6
c = 7
print("a +b +c= ", a + b + c,"a -b -c= ",a - b - c)

#zadanie 5
x1 = 5

x2 = 2

print(x1 // x2)


#zadanie 6
a = 5

b = 6

c = a * b

b -= 2

d = a // c

e = c ** 6

print("_________________")


#zadanie 7
for x in range (0,6):
for y in range (0,6):

print(x * y)


#zadanie 8
liczba1 = int(input())

liczba2 = int(input())

liczba3 = int(input())

print(liczba1 * liczba2 * liczba3)


#zadanie 9
a0 = int(input())

b0 = int(input())

c0 = int(input())

delta = b0 * b0 - 4* (a0 * c0)

ww = math.sqrt(delta)

if delta < 0:

print("Nie ma rozwiązań")

if delta == 0:

x0 = - b0 / 2*a0

print(w0 , " jest rozwiazaniem równania")

if delta > 0:

x1 = (-b - ww) / 2*a0


x2 = (-b + ww) / 2*a0


print(x1 , x2 , "są rozwiązaniami równania")

#zadanie 10
temp = int(input("Podaj temp: "))

konw = (input("Konwekcja(C,K,F): "))


if konw == "C":

print(temp, "C")

print(temp+273.15, "K")

print((temp*9/5)+32, "F")


elif konw == "K":

print(temp-273.15, "C")

print(temp, "K")

print(((temp-273.15) * 9 / 5) + 32, "F")


elif konw == "F":

print(((temp-32)*5/9), "C")

print(((temp-32)*5/9)+273.15, "K")

print(temp, "F")
