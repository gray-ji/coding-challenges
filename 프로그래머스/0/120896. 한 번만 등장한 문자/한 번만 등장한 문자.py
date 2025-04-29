def solution(s):
    duplicates = []
    answer = []
    
    for i in sorted(s):
        if i in answer:
            duplicates.append(i)
        else:
            answer.append(i)
    
    for i, v in enumerate(answer):
        if v in duplicates:
            answer[i] = ''
    
    return ''.join(answer)