def solution(p, c):
    dct = dict()
    for e in p:
        if (e in dct):
            dct[e] += 1
        else:
            dct[e] = 1
    for e in c:
        dct[e] -= 1
    for k in dct:
        if (dct[k] == 1):
            return k

def solution(p, c):
    p.sort()
    c.sort()
    for i in range(len(c)):
        if (p[i] != c[i]):
            return p[i]
    return p[-1]

def solution(p, c):
    from collections import Counter
    dct = Counter(p) - Counter(c)
    return list(dct.keys())[0]
