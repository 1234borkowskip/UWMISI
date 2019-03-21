def silnia(a):
    if a == 0:
        return 1
    return a*silnia(a-1)

print(silnia(3))
print(silnia(10))
print(silnia(5))