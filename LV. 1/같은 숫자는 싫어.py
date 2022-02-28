def solution(lst):
    res = list()
    pre = -1
    for e in lst:
        if (pre == e):
            continue
        res.append(e)
        pre = e
    return res