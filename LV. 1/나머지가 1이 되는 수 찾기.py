def solution(n):
    for i in range(1, n + 1):
        if (n % i == 1):
            return i
    else:
        return 0

def solution(n):
    return [i for i in range(1, n + 1) if (n % i == 1)][0]