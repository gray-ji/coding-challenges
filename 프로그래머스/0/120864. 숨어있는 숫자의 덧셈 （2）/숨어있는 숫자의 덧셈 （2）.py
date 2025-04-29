def solution(my_string):
    tmp = '0'
    answer = 0
    
    for c in my_string:
        if c.isdigit():
            tmp += c
        else:
            answer += int(tmp)
            tmp = '0'
            
    answer += int(tmp)
    
    return answer