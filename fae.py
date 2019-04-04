def rek(n):
    if n == 1: return 1
    if n == 0: return 1
    return 4*rek(n-1)+5

print(rek(2))
print(rek(23))