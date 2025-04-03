def solution(n):
    if n == 1:
        return [[1]]
    
    answer = [[0] * n for _ in range(n)]
    numbers = [(i * n) + j for i in range(n) for j in range(1, n+1)]

    i, j = 0, 0
    dir = 'R'
    s_cnt = {'R': 0, 'D': 0, 'L': 0, 'U': 0}
    
    while answer[i][j] == 0:
        answer[i][j] = numbers.pop(0)

        if dir == 'R':
            if j == (n - 2) - s_cnt['R']:
                dir = 'D'
                s_cnt['U'] += 1
            j += 1
        elif dir == 'D':
            if i == (n - 2) - s_cnt['D']:
                dir = 'L'
                s_cnt['R'] += 1
            i += 1
        elif dir == 'L':
            if j == 1 + s_cnt['L']:
                dir = 'U'
                s_cnt['D'] += 1
            j -= 1
        else:
            if i == 1 + s_cnt['U']:
                dir = 'R'
                s_cnt['L'] += 1
            i -= 1
    
    return answer