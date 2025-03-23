def solution(a, b):
    answer = int(f'{a}{b}')
    if answer < int(f'{b}{a}'):
        answer = int(f'{b}{a}')
    return answer