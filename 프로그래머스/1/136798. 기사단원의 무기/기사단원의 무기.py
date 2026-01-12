def solution(number, limit, power):
    answer = 1
    
    for i in range(2, number+1):
        yagsu = 2
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                yagsu += 1
                if i // j != j:
                    yagsu += 1
                if yagsu > limit:
                    yagsu = power
                    break
        answer += yagsu
    
    return answer