def solution(arr, divisor):
    ret = list(x for x in arr if x % divisor == 0 )
    return sorted(ret) if (ret) else [-1]