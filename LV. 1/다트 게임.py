def solution(dart):
    idx = 0
    r = 0
    res = [0, 0, 0]
    while (idx < len(dart)):
        temp = int(dart[idx])
        idx += 1
        if (dart[idx].isdigit()):
            temp = int(dart[idx - 1: idx + 1])
            idx += 1
        if (dart[idx] == 'D'): temp**=2
        elif (dart[idx] == 'T'): temp**=3
        idx += 1
        res[r] = temp
        
        if (idx < len(dart) and (dart[idx] == '*' or dart[idx] == '#')):
            if (dart[idx] == '*'):
                if (r != 0):
                    res[r - 1] *= 2
                res[r] = temp*2
            elif (dart[idx] == '#'):
                res[r] = -temp
            idx += 1
        r += 1
        print("res", res)
                
    return sum(res)

def oth(dartResult):
    import re
    pat = re.compile('(\d+)([SDT])([#*]?)')
    dart = pat.findall(dartResult)
    area = {'S': 1, "D": 2, "T": 3}
    award = {'': 1, "*": 2, "#": -1}
    
    for i in range(3):
        if (dart[i][2] == '*' and 0 < i):
            dart[i - 1] *= 2
        dart[i] = int(dart[i][0])**area[dart[i][1]]*award[dart[i][2]]
    
    return sum(dart)