def solution(num, k):
    for i, v in enumerate(str(num)):
        if v == str(k):
            return i + 1
    return -1