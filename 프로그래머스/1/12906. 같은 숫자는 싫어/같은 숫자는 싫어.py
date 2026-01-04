def solution(arr):
    return [v for i, v in enumerate(arr) if not i or arr[i-1] != v]