def solution(numlist, n):
    tmp = [[0, num] for num in numlist]
    
    for i, v in enumerate(tmp):
        if v[1] < n:
            tmp[i][0] = (n - tmp[i][1]) + 0.5
        else:
            tmp[i][0] = tmp[i][1] - n
    
    return [num[1] for num in sorted(tmp)]