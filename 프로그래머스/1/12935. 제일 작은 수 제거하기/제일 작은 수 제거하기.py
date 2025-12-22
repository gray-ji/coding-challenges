def solution(arr):
    minimum = min(arr)
    answer = [v for v in arr if v > minimum]
    return answer if answer else [-1]