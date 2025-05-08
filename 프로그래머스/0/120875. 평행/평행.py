def solution(dots):
    idxs = [[1, 2, 3], [2, 1, 3], [3, 1, 2]]

    for i, a, b in idxs:
        m1 = (dots[0][1] - dots[i][1]) / (dots[0][0] - dots[i][0])
        m2 = (dots[a][1] - dots[b][1]) / (dots[a][0] - dots[b][0])

        if m1 == m2:
            return 1
    return 0