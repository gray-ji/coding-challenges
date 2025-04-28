def solution(array):
    answer = [-1, -1]
    
    for i, v in enumerate(array):
        if v > answer[0]:
            answer = [v, i]
    
    return answer