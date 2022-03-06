def solution(arr):
    from math import gcd
    res = arr[0]
    for e in arr:
        res = res*e//gcd(res, e)
    return res
        
