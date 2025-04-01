def solution(n_str):
    i = 0
    
    while True:
        if n_str[i] != '0':
            return n_str[i:]
        i += 1