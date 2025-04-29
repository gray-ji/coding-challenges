def solution(i, j, k):
    answer = 0
    
    for num in range(i, j+1):
        for n in str(num):
            if k == int(n):
                answer += 1
    
    return answer