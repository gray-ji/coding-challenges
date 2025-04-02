def solution(myString):
    answer = ''
    
    for s in myString:
        if s < 'l':
            s = 'l'
        answer += s
    
    return answer