def solution(numlist, n):
    tmp = [[0, num] for num in numlist]
    
    for i, v in enumerate(tmp):
        tmp[i][0] = abs(n - v[1])
        if v[1] < n:
            tmp[i][0] += 0.5
    
    return [num[1] for num in sorted(tmp)]