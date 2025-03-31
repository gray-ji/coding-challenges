def solution(arr):
    for i in range(11):
        size = 2 ** i
        
        if len(arr) == size:
            break
        elif len(arr) < size:
            return arr + [0] * (size - len(arr))
    
    return arr