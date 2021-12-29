def solution(s):
    res = ''
    lst = [4, 3, 3, 5, 4, 4, 3, 5, 5, 4]
    i = 0
    while (i < len(s)):
        if (s[i].isdigit()):
            res += s[i]
            i += 1
        else:
            temp = -1
            if (s[i] == 'z'): temp = 0
            elif (s[i] == "o"): temp = 1
            elif (s[i] == 't'):
                if (s[i + 1] == 'w'): temp = 2
                else: temp = 3
            elif (s[i] == 'f'):
                if (s[i + 1] == 'o'): temp = 4
                else: temp = 5
            elif (s[i] == 's'):
                if (s[i + 1] == 'i'): temp = 6
                else: temp = 7
            elif (s[i] == 'e'): temp = 8
            else: temp = 9
            res += str(temp)
            i += lst[temp]
            
    return int(res)


def solution(s):
    dct = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    for k, v in dct.items():
        s = s.replace(k, v)
    return int(s)