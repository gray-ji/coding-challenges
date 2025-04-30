def solution(spell, dic):
    tmp = sorted(spell)
    
    for d in dic:
        if sorted(d) == tmp:
            return 1
    return 2