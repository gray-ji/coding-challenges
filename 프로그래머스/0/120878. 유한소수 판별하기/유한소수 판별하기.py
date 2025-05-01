def solution(a, b):
    i = 2
    while a >= i and b >= i:
        if a % i == 0 and b % i == 0:
            a //= i
            b //= i
        else:
            i += 1
    
    i = 2
    while b >= i:
        if b % i == 0:
            if i not in [2, 5]:
                return 2
            b //= i
        else:
            i += 1
    
    return 1 if b in [1, 2, 5] else 2