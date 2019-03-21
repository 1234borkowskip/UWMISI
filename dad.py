def cg(n, a1=1, q=2):
    n = n - 1
    while n > 0:
        a1 = a1 * q
        n = n - 1
    return a1


print("{} wyraz ciagu geometrycznego gdzie a1 = {}, q = {} wynosi {}".format(4, 1, 5, cg(4, 1, 5)))
print("{} wyraz ciagu geometrycznego gdzie a1 = {}, q = {} wynosi {}".format(7, 1, 2, cg(7)))