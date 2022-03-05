def solution(sizes):
    width, height = 0, 0
    for e in sizes:
        a, b = e[0], e[1]
        if (a < b): a, b = b, a
        if (width < a):
            width = a
        if (height < b):
            height = b
    return width*height

def solution(sizes):
    return max(max(e) for e in sizes)*max(min(e) for e in sizes)