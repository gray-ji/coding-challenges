def solution(lines):
    cnts = [0] * 201
    answer = 0
    
    for start, end in lines:
        for i in range(start, end):
            cnts[i+100] += 1
    
    for i in cnts:
        if i > 1:
            answer += 1
    
    return answer