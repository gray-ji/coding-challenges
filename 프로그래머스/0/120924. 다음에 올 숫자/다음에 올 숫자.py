def solution(common):
    d = common[1] - common[0]
    
    if d == common[2] - common[1]:
        return common[-1] + d
    return common[-1] * common[1] // common[0]