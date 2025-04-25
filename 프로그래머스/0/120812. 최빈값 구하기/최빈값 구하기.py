def solution(array):
    cnts = [0] * 1000
    mode, cnt = -1, 0
    
    for num in array:
        cnts[num] += 1
    
    for i, v in enumerate(cnts):
        if v > cnt:
            mode, cnt = i, v
        elif v == cnt:
            mode = -1
    
    return mode