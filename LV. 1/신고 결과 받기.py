def solution(id_list, report, k):
    res = dict()
    for e in id_list:
        res[e] = 0
        
    dct = dict()
    for e in report:
        a, b = e.split()
        if (b in dct):
            if (not a in dct[b]) :
                dct[b].append(a)
        else:
            dct[b] = [a]
            
    for key in dct:
        if (len(dct[key]) >= k):
            for e in dct[key]:
                res[e] += 1
                
    return list(res.values())