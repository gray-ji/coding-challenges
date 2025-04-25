def solution(my_string, n):
    answer = ''
    
    for ms in my_string:
        for i in range(n):
            answer += ms
    
    return answer