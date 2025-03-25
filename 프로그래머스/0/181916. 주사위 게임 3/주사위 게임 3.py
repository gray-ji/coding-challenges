def solution(a, b, c, d):
    cnts = [0] * 6
    
    for d in [a, b, c, d]:
        cnts[d - 1] += 1
    
    max_cnt = max(cnts)
    if max_cnt == 4:
        return 1111 * a
    if max_cnt == 1:
        return min(a, b, c, d)

    q, p = 0, 0
    p_v = 3 if max_cnt == 3 else 2
    for i, v in enumerate(cnts):
        if not p and v == p_v:
            p = i + 1
        elif not q and v in [1, 2]:
            q = i + 1
        elif v == 1:
            r = i + 1
    
    if max_cnt == 3:
        return (10 * p + q) ** 2

    cnts = [d > 0 for d in cnts]
    if sum(cnts) == 2:
        return (p + q) * abs(p - q)
    return q * r