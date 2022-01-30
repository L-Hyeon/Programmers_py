def solution(n):
    t = ''
    while (n):
        t = str(n % 3) + t
        n //= 3
    res = 0
    for i in range(len(t)):
        res += (3**i)*int(t[i])
    
    return res

def oth(n):
    t = ''
    while (n):
        t += str(n % 3)
        n //= 3
    
    return int(t, 3)