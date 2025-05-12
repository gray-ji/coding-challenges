def solution(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for x in range(max(0, i-1), min(n, i+2)):
                    for y in range(max(0, j-1), min(n, j+2)):
                        if board[x][y] == 0:
                            board[x][y] = 2
    
    answer = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1
    
    return answer