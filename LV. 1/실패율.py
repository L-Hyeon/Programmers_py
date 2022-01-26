def solution(N, stages):
    res = dict()
    people = len(stages)
    for i in range(1, N + 1):
        if (people == 0):
            res[i] = 0
        else:
            stuck = stages.count(i)
            res[i] = stuck/people
            people -= stuck
    
    return sorted(res, key = lambda x: res[x], reverse = True)
