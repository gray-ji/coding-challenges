def solution(s):
    sets = [list(map(int, v.split(','))) for v in s[2:-2].split('},{')]
    added = set()
    result = []
    
    for v1 in sorted(sets, key=lambda x:len(x)):
        for v2 in v1:
            if v2 not in added:
                added.add(v2)
                result.append(v2)
    return result