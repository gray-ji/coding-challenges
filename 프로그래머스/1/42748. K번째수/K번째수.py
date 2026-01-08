def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        tmp = sorted(array[i-1:j])
        answer.append(tmp[min(k-1, len(tmp))])
    
    return answer