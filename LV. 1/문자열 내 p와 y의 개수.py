def solution(s):
    cntP = s.count('p') + s.count('P')
    cntY = s.count('y') + s.count('Y')
    return cntP == cntY