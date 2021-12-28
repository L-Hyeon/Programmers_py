def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zCnt = 0
    win_nums = set(win_nums)
    for e in lottos:
        if (e == 0):
            zCnt += 1
        elif (e in win_nums):
            cnt += 1
    
    rank = [6, 6, 5, 4, 3, 2, 1]
    answer = [rank[zCnt + cnt], rank[cnt]]
    
    return answer