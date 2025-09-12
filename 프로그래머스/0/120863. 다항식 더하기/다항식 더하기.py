def solution(polynomial):
    terms = polynomial.split(' + ')
    linear, constant = 0, 0
    
    for term in terms:
        if 'x' in term:
            linear += int(term[:-1]) if term[:-1] else 1
        else:
            constant += int(term)

    result = []
    if linear:
        result.append('x' if linear == 1 else f'{linear}x')
    if constant:
        result.append(f'{constant}')
    
    return ' + '.join(result)