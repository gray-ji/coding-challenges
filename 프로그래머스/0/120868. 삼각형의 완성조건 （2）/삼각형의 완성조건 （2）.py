def solution(sides):
    max_side, min_side = max(sides), min(sides)
    answer = 0
    
    i = max_side
    while max_side < min_side + i:
        answer += 1
        i -= 1
    
    i = max_side + 1
    while i < max_side + min_side:
        answer += 1
        i += 1
    
    return answer