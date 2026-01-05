def solution(s):
    answer = []
    idx = 0
    
    for c in s:
        idx = 0 if c == ' ' else (idx + 1)
        answer.append(c.upper() if idx % 2 else c.lower())
        
    return ''.join(answer)