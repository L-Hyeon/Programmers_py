def solution(n, m):
    from math import gcd
    g = gcd(n, m)
    return [g, n*m/g]

def solution(n, m):
    a, b = max(n, m), min(n, m)
    while (b != 0):
        a, b = b, a % b
    return [a, n*m/a]