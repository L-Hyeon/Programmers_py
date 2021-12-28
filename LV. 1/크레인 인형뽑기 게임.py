def solution(board, moves):
    stk = list()
    res = 0
    size = len(board)
    for e in moves:
        for i in range(size):
            if (board[i][e - 1]):
                if (stk) and (stk[-1] == board[i][e - 1]):
                    stk.pop()
                    res += 2
                else:
                    stk.append(board[i][e - 1])
                board[i][e - 1] = 0
                break
    
    return res