def solution(number):
    n = len(number)
    answer = 0
    
    for a in range(n - 2):
        for b in range(a + 1, n - 1):
            for c in range(b + 1, n):
                if not number[a] + number[b] + number[c]:
                    answer += 1
    
    return answer