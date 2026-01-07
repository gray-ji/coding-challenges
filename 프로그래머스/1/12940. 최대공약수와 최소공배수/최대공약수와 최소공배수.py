def solution(n, m):
    GCD, LCM = 1, n * m
    big, small = max(n, m), min(n, m)
    
    for i in range(2, small+1):
        if not (small % i or big % i):
            GCD = i
    
    for i in range(1, small):
        isLCM = False
        for j in range(i, big):
            if small * j > big * i:
                break
            if big * i == small * j:
                LCM = big * i
                isLCM = True
        if isLCM:
            break
    
    return [GCD, LCM]