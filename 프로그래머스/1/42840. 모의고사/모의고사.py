def solution(answers):
    cnts = [0, 0, 0]
    patterns = ((1, 2, 3, 4, 5),
                (2, 1, 2, 3, 2, 4, 2, 5),
                (3, 3, 1, 1, 2, 2, 4, 4, 5, 5))
    
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if pattern[i % len(pattern)] == answer:
                cnts[j] += 1
    
    cnt_max = max(cnts)
    return [i+1 for i, v in enumerate(cnts) if v == cnt_max]