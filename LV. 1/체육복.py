def solution(n, l, r):
    lost = set(l) - set(r)
    reserve = set(r) - set(l)

    for e in lost:
        if (e - 1 in reserve):
            reserve.remove(e - 1)
        elif (e + 1 in reserve):
            reserve.remove(e + 1)
        else:
            n -= 1

    return n
