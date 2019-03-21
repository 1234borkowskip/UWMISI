def czy_palindrom(wyraz):
    wyraz = wyraz.upper()
    if wyraz == wyraz[::-1]:
        return 1
    return 0


wyraz = "palindrom"
if czy_palindrom(wyraz) == 1:
    print(wyraz, "jest palindromem")
else:
    print(wyraz, "nie jest palindromem")

wyraz = "kajak"
if czy_palindrom(wyraz) == 1:
    print(wyraz, "jest palindromem")
else:
    print(wyraz, "nie jest palindromem")
