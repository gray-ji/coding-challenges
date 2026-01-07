def solution(food):
    answer = ['0' for _ in range(len(food) * 2 + 1)]
    
    for i, v in enumerate(food):
        a = str(i) * (v // 2)
        answer[i] = a
        answer[-1-i] = a
    
    return ''.join(answer)