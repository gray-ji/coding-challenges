def solution(n):
    answer = 1
    
    for i in range(1, n):
        hab = i
        for j in range(i+1, n):
            hab += j
            if hab >= n:
                if hab == n:
                    answer += 1
                break
    
    return answer