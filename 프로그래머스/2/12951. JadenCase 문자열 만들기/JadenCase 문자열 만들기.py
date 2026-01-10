def solution(s):
    start = True
    answer = []
    
    for c in s:
        if c == ' ':
            start = True
        else:
            c = c.upper() if start else c.lower()
            start = False
            
        answer.append(c)
    
    return ''.join(answer)