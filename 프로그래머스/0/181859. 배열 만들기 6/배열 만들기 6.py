def solution(arr):
    stk = []
    
    for i, v in enumerate(arr):
        if not stk or stk[-1] != v:
            stk.append(v)
        else:
            stk.pop()
    
    return stk if stk else [-1]