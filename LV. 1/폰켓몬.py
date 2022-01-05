def solution(n):
    res = 0
    l = len(n)//2
    n = set(n)
    res = len(n) if (len(n) < l) else l
    
    return res