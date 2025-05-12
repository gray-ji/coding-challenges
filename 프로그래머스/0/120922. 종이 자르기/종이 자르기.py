def solution(M, N):
    max_side, min_side = max(M, N), min(M, N)
    
    return (min_side - 1) + (max_side - 1) * min_side