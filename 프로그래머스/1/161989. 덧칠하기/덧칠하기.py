def solution(n, m, section):
    num = 0
    answer = 0
    
    for s in section:
        if num < s:
            num = s + m - 1
            answer += 1
    
    return answer