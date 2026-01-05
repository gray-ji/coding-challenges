def solution(n):
    sam = []
    answer = 0
    
    while n > 0:
        sam.append(n % 3)
        n //= 3
        
    for i in range(len(sam)):
        answer += sam[-i - 1] * (3 ** i)
    
    return answer