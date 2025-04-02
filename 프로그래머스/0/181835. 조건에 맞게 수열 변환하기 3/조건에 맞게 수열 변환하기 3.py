def solution(arr, k):
    if k % 2 == 0:
        return [a + k for a in arr]
    return [a * k for a in arr]