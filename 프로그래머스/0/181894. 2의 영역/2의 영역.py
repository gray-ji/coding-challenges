def solution(arr):
    start, end = -1, -1
    
    for i in range(len(arr)):
        if arr[i] == 2:
            if start < 0:
                start = i
            else:
                end = i

    if start == -1:
        return [-1]
    elif end == -1:
        return [2]
    return arr[start:end+1]