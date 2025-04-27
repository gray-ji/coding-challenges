def solution(num_list, n):
    answer = []

    for i in range(len(num_list)):
        if (i + 1) % n == 0:
            answer.append(num_list[i-n+1:i+1])
    
    return answer