def fun(liczby):
    n = len(str(liczby))
    dziel=1
    tak = 10
    suma = 0
    cos = liczby
    for x in range(0,n):
        liczba=liczby%tak
        liczby-=liczba
        tak*=10
        liczba/=dziel
        suma+=liczba
        dziel*=10

    return int(suma)

print(fun(545435433))
