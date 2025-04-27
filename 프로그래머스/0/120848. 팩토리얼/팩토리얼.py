def solution(n):
    factorial, answer = 1, 1
    
    while True:
        if factorial >= n:
            if factorial > n:
                answer -= 1
            break
        answer += 1
        factorial *= answer
    
    return answer