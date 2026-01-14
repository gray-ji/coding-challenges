def solution(board, moves):
    answer = 0
    basket = []
    
    for move in moves:
        for i in range(len(board)):
            doll = board[i][move-1]
            if doll:
                board[i][move-1] = 0
                if basket and basket[-1] == doll:
                    answer += 2
                    basket.pop()
                else:
                    basket.append(doll)
                break
    
    return answer