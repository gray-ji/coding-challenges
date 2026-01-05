def solution(d, budget):
    answer = 0
    
    for v in sorted(d):
        if budget < v:
            break
        budget -= v
        answer += 1
    
    return answer