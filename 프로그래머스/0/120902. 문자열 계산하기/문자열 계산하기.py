def solution(my_string):
    tmp = my_string.split()
    answer = int(tmp[0])
    
    for i in range(2, len(tmp), 2):
        if tmp[i-1] == '+':
            answer += int(tmp[i])
        elif tmp[i-1] == '-':
            answer -= int(tmp[i])
    
    return answer