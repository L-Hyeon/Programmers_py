def solution(answers):
    pick = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    l = [5, 8, 10]
    right = [0]*3
    mx = 0
    for i in range(len(answers)):
        if (answers[i] == pick[0][i % l[0]]):
            right[0] += 1
            if (mx < right[0]):
                mx = right[0]
        if (answers[i] == pick[1][i % l[1]]):
            right[1] += 1
            if (mx < right[1]):
                mx = right[1]
        if (answers[i] == pick[2][i % l[2]]):
            right[2] += 1
            if (mx < right[2]):
                mx = right[2]
        
    res = list()
    for i in range(3):
        if (right[i] == mx):
            res += [i + 1]
    return res
  

