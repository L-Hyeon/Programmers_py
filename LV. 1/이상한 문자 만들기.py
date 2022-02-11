def solution(s):
    res = list()
    words = list(s.split(' '))
    for i in range(len(words)):
        t = ''
        for j in range(len(words[i])):
            if (j % 2):
                t += words[i][j].lower()
            else:
                t += words[i][j].upper()
        res += [t]
    
    return ' '.join(res)
