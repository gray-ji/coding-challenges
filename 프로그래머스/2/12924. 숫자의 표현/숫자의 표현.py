def solution(n):
    answer = 0
    start, end = 1, 1
    hab = 1
    
    while start <= n:
        if hab >= n:
            if hab == n:
                answer += 1
            hab -= start
            start += 1
        else:
            end += 1
            hab += end
    
    return answer