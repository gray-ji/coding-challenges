def solution(sizes):
    w, l = 1, 1
    
    for size in sizes:
        x, y = max(size), min(size)
        w, l = max(x, w), max(y, l)
    
    return w * l