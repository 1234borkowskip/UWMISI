def fun(n):
    re = [ x  for x in range(4,77) if x % n == 0]
    return re

print(fun(7))