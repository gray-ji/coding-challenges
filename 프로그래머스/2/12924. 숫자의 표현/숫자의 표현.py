def solution(n):
    answer = 1
    
    for i in range(1, n):
        for j in range(i, n):
            hab = sum(range(i, j+1))
            if hab >= n:
                if hab == n:
                    answer += 1
                break
    
    return answer