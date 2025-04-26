def solution(emergency):
    tmp = sorted(emergency, reverse=True)
    
    return [j + 1 for i in emergency for j, v in enumerate(tmp) if i == v]