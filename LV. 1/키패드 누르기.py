def solution(num, hand):
    res = ''
    pos = [[3, 0], [3, 2]]
    for e in num:
        if (e in (1, 4, 7)):
            res += 'L'
            if (e == 1): pos[0] = [0, 0]
            elif (e == 4): pos[0] = [1, 0]
            else: pos[0] = [2, 0]
        elif (e in (3, 6, 9)):
            res += "R"
            if (e == 3): pos[1] = [0, 2]
            elif (e == 6): pos[1] = [1, 2]
            else: pos[1] = [2, 2]
        else:
            if (e == 2):
                t = [0, 1]
                t1 = pos[0][0] + (1 - pos[0][1])
                t2 = pos[1][0] + (pos[1][1] - 1)
            elif (e == 5):
                t = [1, 1]
                t1 = abs(1 - pos[0][0]) + abs(1 - pos[0][1])
                t2 = abs(1 - pos[1][0]) + abs(1 - pos[1][1])
            elif (e == 8):
                t = [2, 1]
                t1 = abs(2 - pos[0][0]) + abs(1 - pos[0][1])
                t2 = abs(2 - pos[1][0]) + abs(1 - pos[1][1])
            else:
                t = [3, 1]
                t1 = abs(3 - pos[0][0]) + abs(1 - pos[0][1])
                t2 = abs(3 - pos[1][0]) + abs(1 - pos[1][1])
                
            if (t1 < t2):
                res += "L"
                pos[0] = t
            elif (t1 > t2):
                res += "R"
                pos[1] = t
            else:
                if (hand == "right"):
                    res += "R"
                    pos[1] = t
                else:
                    res += "L"
                    pos[0] = t
                
    return res