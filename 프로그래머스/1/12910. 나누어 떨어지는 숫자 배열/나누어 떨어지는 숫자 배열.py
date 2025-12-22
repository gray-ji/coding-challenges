def solution(arr, divisor):
    answer = [n for n in arr if not n % divisor]
            
    if not len(answer):
        return [-1]
    return sorted(answer)