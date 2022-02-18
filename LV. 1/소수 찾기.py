def solution(n):
    seive = [False, False] + [True]*(n - 1)
    for i in range(2, int(n**0.5) + 1):
        if (seive[i]):
            for j in range(i + i, n + 1, i):
                seive[j] = False
    return seive.count(True)