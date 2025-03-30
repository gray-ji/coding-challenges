def solution(myString, pat):
    tmp = list(myString)
    
    for i, v in enumerate(tmp):
        tmp[i] = 'B' if v == 'A' else 'A'
    
    return int(pat in ''.join(tmp))