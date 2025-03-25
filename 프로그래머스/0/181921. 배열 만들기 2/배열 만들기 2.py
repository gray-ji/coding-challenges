def solution(l, r):
    answer = []
    
    for i in range(l, r + 1):
        is_append = True
        
        for n in ['1', '2', '3', '4', '6', '7', '8', '9']:
            if n in str(i):
                is_append = False
                break
        
        if is_append:
            answer.append(i)
            if str(i).endswith('50'):
                i += 50
            else:
                i += 5
    
    return answer if answer else [-1]