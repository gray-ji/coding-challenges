def solution(cards1, cards2, goal):
    cards1 = cards1[::-1]
    cards2 = cards2[::-1]
    
    for v in goal:
        if cards1 and cards1[-1] == v:
            cards1.pop()
        elif cards2 and cards2[-1] == v:
            cards2.pop()
        else:
            return 'No'
        
    return 'Yes'