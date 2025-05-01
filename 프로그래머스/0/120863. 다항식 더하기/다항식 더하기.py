def solution(polynomial):
    tmp = polynomial.split()
    linear, constant = 0, 0
    
    for i in range(0, len(tmp), 2):
        if 'x' in tmp[i]:
            if tmp[i] == 'x':
                linear += 1
            else:
                linear += int(tmp[i][:-1])
        else:
            constant += int(tmp[i])

    if linear != 0:
        linear = 'x' if linear == 1 else f'{linear}x'
        
    if linear != 0 and constant != 0:
        return f'{linear} + {constant}'
    if linear != 0:
        return f'{linear}'
    return f'{constant}'