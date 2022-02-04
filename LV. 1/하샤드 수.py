def solution(x):
    answer = True
    temp = 0
    for e in str(x):
        temp += int(e)
    if (x % temp):
        answer = False
    return answer

def solution(x):
    return x % sum(int(e) for e in str(x)) == 0