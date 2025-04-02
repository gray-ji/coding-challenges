def solution(picture, k):
    answer = []
    
    for pic in picture:
        line = ''
        
        for i, v in enumerate(pic):
            for _ in range(k):
                line += v
                
        for _ in range(k):
            answer.append(line)
    
    return answer