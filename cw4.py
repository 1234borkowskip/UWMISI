
def silnia(x):
    if x is 1:
        return 1
    else:
        return x*silnia(x-1)

print("1! =",silnia(1))
print("3! =",silnia(3))
print("9! =",silnia(9))


#zadanie 3 (dac.py)

def silniarek(x):
    if x is 1:
        return 1
    else:
        return x*silniarek(x-1)


x = int(input('Silnia '))
print(x,"! wynosi ", silniarek(x))

#zadanie 4 (dad.py)

def cg(a1, q, an)
a1 = 1
g = 2


