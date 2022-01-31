def solution(d, budget):
    res = 0
    for e in sorted(d):
        if (budget >= e):
            budget -= e
            res += 1
    return res