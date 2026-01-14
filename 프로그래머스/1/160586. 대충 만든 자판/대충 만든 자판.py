def solution(keymap, targets):
    answer = []
    
    for target in targets:
        cnt = 0
        for t in target:
            idx = -1
            for k in keymap:
                f_idx = k.find(t)
                if idx == -1:
                    idx = f_idx
                elif -1 < f_idx < idx:
                    idx = f_idx
            if idx == -1:
                cnt = -1
                break
            cnt += (idx + 1)
        answer.append(cnt)
    
    return answer