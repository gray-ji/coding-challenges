def solution(numbers, k):
    answer = 1
    
    for i in range(1, k):
        answer += 2
        if len(numbers) < answer:
            answer %= len(numbers)
    
    return answer