def solution(n):
    answer = sorted([i for i in str(n)], reverse=True)
    return int(''.join(answer))