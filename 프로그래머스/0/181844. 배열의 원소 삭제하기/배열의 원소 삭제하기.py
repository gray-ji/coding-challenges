def solution(arr, delete_list):
    answer = [v for v in arr if v not in delete_list]
    return answer