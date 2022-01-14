def solution(n):
    digit = [True]*10
    for e in n:
        digit[e] = False
    res = 0
    for i in range(10):
        if (digit[i]):
            res += i
    return res

def fast(n):
  return 45 - sum(n)
