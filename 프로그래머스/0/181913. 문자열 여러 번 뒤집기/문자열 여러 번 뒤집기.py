def solution(my_string, queries):
    answer = list(my_string)
    for s, e in queries:
        answer[s:e+1] = reversed(answer[s:e+1])
    
    return ''.join(answer)