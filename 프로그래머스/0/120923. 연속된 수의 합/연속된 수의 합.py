def solution(num, total):
    answer = []
    start = -50
    
    while True:
        answer = list(range(start, start + num))
        if sum(answer) == total:
            return answer
        start +=1

    return answer