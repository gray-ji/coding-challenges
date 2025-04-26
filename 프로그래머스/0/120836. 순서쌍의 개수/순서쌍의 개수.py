def solution(n):
    answer = 1 if n == 1 else 2
    
    for a in range(2, n // 2 + 1):
        if n % a == 0:
            answer += 1
    
    return answer