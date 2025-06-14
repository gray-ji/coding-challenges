def solution(numbers):
    answer = 0
    is_num = [False for i in range(10)]
    
    for i in numbers:
        is_num[i] = True
    
    for i in range(10):
        if not is_num[i]:
            answer += i
    
    return answer