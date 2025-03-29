def solution(myString):
    answer = ''
    
    for s in myString:
        if s in ['a', 'A']:
            s = 'A'
        elif s.isupper():
            s = s.lower()
        answer += s
    
    return answer