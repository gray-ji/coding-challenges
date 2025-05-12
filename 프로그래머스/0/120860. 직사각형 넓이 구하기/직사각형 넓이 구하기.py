def solution(dots):
    sides = [0, 0]
    
    if dots[0][0] == dots[1][0]:
        sides[0] = abs(dots[0][1] - dots[1][1])
    elif dots[0][0] == dots[2][0]:
        sides[0] = abs(dots[0][1] - dots[2][1])
    else:
        sides[0] = abs(dots[0][1] - dots[3][1])
    
    if dots[0][1] == dots[1][1]:
        sides[1] = abs(dots[0][0] - dots[1][0])
    elif dots[0][1] == dots[2][1]:
        sides[1] = abs(dots[0][0] - dots[2][0])
    else:
        sides[1] = abs(dots[0][0] - dots[3][0])
    
    return sides[0] * sides[1]