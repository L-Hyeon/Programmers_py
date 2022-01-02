def solution(lst, commands):
    res = list()
    for e in commands:
        temp = lst[e[0] - 1 : e[1]]
        temp.sort()
        res.append(temp[e[2] - 1])
    return res