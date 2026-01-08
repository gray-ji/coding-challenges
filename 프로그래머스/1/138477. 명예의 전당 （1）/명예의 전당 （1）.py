def solution(k, score):
    top = []
    answer = []
    
    for i, v in enumerate(score):
        if i < k or v > top[0]:
            top.append(v)
            top.sort()
            if len(top) > k:
                top.pop(0)
        answer.append(top[0])
    
    return answer