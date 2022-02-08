def solution(arr):
    mn = min(arr)
    if (len(arr) == 1):
        return [-1]
    return list(x for x in arr if (x != mn))