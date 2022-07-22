def solution(n, apeach):
    answer = [0]*11
    ryan = [0]*11
    maxDiff = 0
    
    # 0 ~ 10점을 획득하는 모든 경우의 수
    for s in range(1, 1<<10):
        score = [0, 0] # 해당 경우에서의 라이언, 어피치의 점수
        arrows = 0 # 사용한 화살 수
        
        # 해당 경우에서의 점수 계산
        for i in range(10):
            # 라이언이 획득
            if (s & 1<<i):
                score[0] += 10 - i
                ryan[i] = apeach[i] + 1
                arrows += ryan[i]
                if (n < arrows):
                    break
            # 어피치가 획득
            else:
                ryan[i] = 0
                if (apeach[i]):
                    score[1] += 10 - i
        
        if (n < arrows):
            continue
        
        # 남은 화살은 모두 0점
        ryan[10] = n - arrows
        
        # 최대 점수차인지 확인
        diff = score[0] - score[1]
        # 최대 점수차 갱신
        if (maxDiff < diff):
            maxDiff = diff
            answer = ryan[:]
        # 최대 점수차와 같은 경우
        elif (maxDiff == diff):
            # 가장 낮은 점수를 많이 쏜 쪽을 answer로 저장
            for i in range(10, -1, -1):
                if (ryan[i] > answer[i]):
                    answer = ryan[:]
                    break
                elif (ryan[i] < answer[i]):
                    break
        
    if (maxDiff == 0):
        return [-1]
        
    return answer