def solution(hp):
    answer = 0
    
    while True:
        if hp >= 5:
            answer += hp // 5
            hp %= 5
        elif hp >= 3:
            answer += hp // 3
            hp %= 3
        else:
            answer += hp
            break
    
    return answer