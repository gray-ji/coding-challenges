def solution(quiz):
    answer = []
    
    for q in quiz:
        a, o, b, _, r = q.split()
        if o == '+' and int(a) + int(b) == int(r):
            answer.append('O')
        elif o == '-' and int(a) - int(b) == int(r):
            answer.append('O')
        else:
            answer.append('X')
    
    return answer