def solution(absolutes, signs):
    answer = 0
    
    for i, v in enumerate(absolutes):
        if not signs[i]:
            v = -v
        answer += v
    
    return answer