def solution(babbling):
    answer = 0
    
    for v in babbling:
        while v:
            word_2, word_3 = v[:2], v[:3]
            if word_2 in ['ye', 'ma']:
                v = v[2:]
            elif word_3 in ['aya', 'woo']:
                v = v[3:]
            else:
                break
                
        if v == '':
            answer += 1
    
    return answer