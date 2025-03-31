def solution(arr, n):
    answer = []
    division = len(arr) % 2
    
    for i, v in enumerate(arr):
        if i % 2 != division:
            v += n
        answer.append(v)
        
    return answer