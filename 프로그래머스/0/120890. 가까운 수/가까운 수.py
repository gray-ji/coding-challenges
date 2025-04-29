def solution(array, n):
    answer = 101
    
    for i in array:
        if i == n:
            answer = i
            break
            
        if i < n:
            if answer < n and (n - i) < (n - answer):
                answer = i
            elif answer > n and (n - i) <= (answer - n):
                answer = i
        else:
            if answer < n and (i - n) < (n - answer):
                answer = i
            elif answer > n and (i - n) <= (answer - n):
                answer = i
    
    return answer