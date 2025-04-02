def solution(date1, date2):
    for i in range(3):
        if date1[i] > date2[i]:
            break
        elif date1[i] < date2[i]:
            return 1
    return 0