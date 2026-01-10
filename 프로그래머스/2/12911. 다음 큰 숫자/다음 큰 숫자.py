def solution(n):
    n_cnt = f'{n:b}'.count('1')

    for i in range(n+1, 1000001):
        if n_cnt == f'{i:b}'.count('1'):
            return i