def solution(arr):
    x = 0
    
    while True:
        tmp = []
        for a in arr:
            if a >= 50 and a % 2 == 0:
                a = a // 2
            elif a < 50 and a % 2 == 1:
                a = a * 2 + 1
            tmp.append(a)

        if tmp == arr:
            break
        arr = tmp
        x += 1
            
    return x