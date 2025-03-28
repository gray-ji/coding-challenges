def solution(num_list):
    sums = [0, 0]
    
    for i, v in enumerate(num_list):
        if i % 2 == 0:
            sums[0] += v
        else:
            sums[1] += v
    
    return sums[0] if sums[0] >= sums[1] else sums[1]