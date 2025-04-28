def solution(s):
    s = s.split()
    answer, before = 0, 0
    
    for c in s:
        if c == 'Z':
            answer -= before
            before = 0
        else:
            answer += int(c)
            before = int(c)
    
    return answer