def solution(str_list, ex):
    answer = ''
    
    for v in str_list:
        if ex not in v:
            answer += v
    
    return answer