def cos(l):
    tak = []
    l.sort()
    min = l[0]
    l.reverse()
    max = l[0]
    tak.append(min)
    tak.append(max)
    print(tak)

l = [2,3,56,-33,3,42,66,43,52,53,454142,1,5]
cos(l)