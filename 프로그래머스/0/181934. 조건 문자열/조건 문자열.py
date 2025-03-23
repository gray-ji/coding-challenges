def solution(ineq, eq, n, m):
    operator = f'{ineq}{eq}'
    
    if operator == '>=':
        return int(n >= m)
    elif operator == '<=':
        return int(n <= m)
    elif operator == '>!':
        return int(n > m)
    return int(n < m)