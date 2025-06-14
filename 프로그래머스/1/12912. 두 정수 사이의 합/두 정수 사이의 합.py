def solution(a, b):
    min_n, max_n = min(a, b), max(a, b)
    answer = max_n
    
    for i in range(min_n, max_n):
        answer += i
    
    return answer