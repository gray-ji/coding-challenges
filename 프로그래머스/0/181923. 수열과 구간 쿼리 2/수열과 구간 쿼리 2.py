def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        answer_part = [arr[i] for i in range(s, e + 1) if arr[i] > k]
        
        answer.append(-1 if len(answer_part) == 0 else min(answer_part))
            
    return answer