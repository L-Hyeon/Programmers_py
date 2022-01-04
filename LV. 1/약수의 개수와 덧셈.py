def solution(left, right):
    res = 0
    for e in range(left, right + 1):
        cnt = 0
        for i in range(1, e + 1):
            if (e % i == 0): cnt += 1
        if (cnt % 2 == 0): res += e
        else: res -= e
    return res
