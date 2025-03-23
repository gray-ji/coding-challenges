def solution(a, b):
    answer = int(f'{a}{b}')
    if answer < 2 * a * b:
        answer = 2 * a * b
    return answer