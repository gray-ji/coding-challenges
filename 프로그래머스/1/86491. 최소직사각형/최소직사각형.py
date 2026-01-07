def solution(sizes):
    w, l = 1, 1
    
    for size in sizes:
        x, y = max(size), min(size)
        w = x if x > w else w
        l = y if y > l else l
    
    return w * l