def solution(s):
    p_cnt, y_cnt = 0, 0
    
    for i in s:
        if i in ['P', 'p']:
            p_cnt += 1
        elif i in ['Y', 'y']:
            y_cnt += 1

    return p_cnt == y_cnt