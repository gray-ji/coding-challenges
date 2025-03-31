def solution(arr, flag):
    answer = []
    
    for i, v in enumerate(arr):
        if flag[i]:
            answer += [v] * (v * 2)
        else:
            for _ in range(min(v, len(answer))):
                answer.pop()
    
    return answer