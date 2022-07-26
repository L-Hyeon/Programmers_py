def solution(s):
    answer = s[0].upper()
    pre = False
    
    for e in s[1:]:
        if (e == ' '):
            pre = True
            answer += ' '
        elif (pre):
            answer += e.upper()
            pre = False
        elif (e.isupper()):
            answer += e.lower()
        else:
            answer += e

    return answer

