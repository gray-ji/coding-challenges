def solution(numbers):
    n = len(numbers)        
    return sorted({
        numbers[i] + numbers[j]
        for i in range(n-1) for j in range(i+1, n)
    })