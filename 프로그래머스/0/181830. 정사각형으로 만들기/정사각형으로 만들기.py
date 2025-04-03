def solution(arr):
    row, col = len(arr), len(arr[0])
    
    if row > col:
        for i in range(row):
            arr[i] += [0] * (row - col)
    elif row < col:
        for _ in range(col - row):
            arr.append([0] * col)
    
    return arr