def solution(rank, attendance):
    tmp = [[v, i] for i, v in enumerate(rank) if attendance[i]]
    tmp.sort()
    
    return 10000 * tmp[0][1] + 100 * tmp[1][1] + tmp[2][1]