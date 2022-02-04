def solution(arr1, arr2):
    answer = list(list(arr1[i][j] + arr2[i][j] for j in range(len(arr1[i]))) for i in range(len(arr1)))
    return answer