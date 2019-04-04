s = {'a': 'y', "e": "i", "i": "o", "o": "a", "y": "e"}
napis = input("podaj :")

for x in range(0,len(napis)):
    if napis[x] in s:
        napis=napis[:x]+s[napis[x]]+napis[x+1:]


print(napis)

s = {'y': 'a', "i": "e", "o": "i", "a": "o", "e": "y"}
napis = input("podaj :")

for x in range(0,len(napis)):
    if napis[x] in s:
        napis=napis[:x]+s[napis[x]]+napis[x+1:]

print(napis)
