def solution(s):
    cnt = {}
    answer = []
    
    for i, c in enumerate(s):
        answer.append((i - cnt[c]) if c in cnt else -1)
        cnt[c] = i
    
    return answer