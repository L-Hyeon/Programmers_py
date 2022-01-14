def solution(a, b):
    res = 0
    for i in range(len(a)):
        res += a[i]*b[i]
    return res

def fast(a, b):
    return sum([i*j for i, j in zip(a, b)])
