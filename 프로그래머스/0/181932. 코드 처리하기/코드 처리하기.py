def solution(code):
    mode = 0
    ret = ''
    
    for idx, val in enumerate(code):
        if val == '1':
            mode = 1 if mode == 0 else 0
        
        elif idx % 2 == mode:
            ret += val
    
    return ret if ret != '' else 'EMPTY'