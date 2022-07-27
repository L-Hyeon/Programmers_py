def solution(arr1, arr2):
    N = len(arr1)
    M = len(arr2[0])
    res = list(list(0 for i in range(M)) for j in range(N))

    for i in range(N):
        for j in range(M):
            temp = 0
            for k in range(len(arr1[0])):
                temp += arr1[i][k]*arr2[k][j]
            res[i][j] = temp

    return res