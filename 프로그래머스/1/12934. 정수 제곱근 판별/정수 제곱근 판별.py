def solution(n):
    for i in range(2, n // 2 + 1):
        if i ** 2 == n:
            return (i + 1) ** 2
    return 4 if n == 1 else -1