def solution(angle):
    answer = 4
    
    if angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif angle < 180:
        answer = 3
    
    return answer