def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        t1 = bin(arr1[i])[2:].zfill(n)
        t2 = bin(arr2[i])[2:].zfill(n)
        print(t1, t2)
        temp = ''
        for j in range(n):
            temp += ' ' if (t1[j] == '0' and t2[j] == '0') else '#'
        answer.append(temp)
        
    return answer


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        t = bin(arr1[i] | arr2[i])[2:].zfill(n)
        t = t.replace('1', '#')
        t = t.replace('0', ' ')
        answer.append(t)
        
    return answer