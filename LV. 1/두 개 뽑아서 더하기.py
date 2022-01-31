def solution(numbers):
    from itertools import combinations
    res = set()
    for e in combinations(numbers, 2):
        res.add(sum(e))
    return sorted(res)