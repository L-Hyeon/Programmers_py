def solution(n):
    from math import sqrt
    s = sqrt(n)
    if (s % 1 == 0):
        return (s + 1)**2
    else:
        return -1