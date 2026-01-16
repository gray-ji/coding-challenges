def rank(cnt):
    return 7 - cnt if cnt > 1 else 6

def solution(lottos, win_nums):
    cnt = len(set(lottos) & set(win_nums))
    return [rank(cnt + lottos.count(0)), rank(cnt)]