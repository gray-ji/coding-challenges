def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        yagsu = 1
        for j in range(2, i+1):
            if i % j == 0:
                yagsu += 1
        if yagsu % 2:
            answer -= i
        else:
            answer += i
    
    return answer