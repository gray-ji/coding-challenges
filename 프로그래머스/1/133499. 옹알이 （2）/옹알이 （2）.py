def solution(babbling):
    answer = 0
    
    for v in babbling:
        next = ''
        while v:
            two, three = v[-2:], v[-3:]
            if two in ('ye', 'ma') and next != two:
                next, v = two, v[:-2]
            elif three in ('aya', 'woo') and next != three:
                next, v = three, v[:-3]
            else:
                break
        if not v:
            answer += 1
    
    return answer