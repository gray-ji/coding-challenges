def solution(balls, share):
    n, m, n_m = 1, 1, 1
    
    for i in range(1, balls):
        n *= i + 1
    for i in range(1, share):
        m *= i + 1
    for i in range(1, balls - share):
        n_m *= i + 1
    
    return n // (n_m * m)