def solution(score):
    answer = [0] * len(score)

    avgs = [(v[0] + v[1], i) for i, v in enumerate(score)]
    avgs.sort(reverse = True)
    
    rank, dup = 1, 1
    for i, v in enumerate(avgs):
        answer[v[1]] = rank
        
        if (i + 1) < len(avgs) and avgs[i+1][0] == v[0]:
            dup += 1
        else:
            rank += dup
            dup = 1
    
    return answer