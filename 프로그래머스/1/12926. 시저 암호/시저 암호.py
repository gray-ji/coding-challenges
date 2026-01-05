def solution(s, n):
    answer = []
    
    for c in s:
        if c.isalpha():
            Aa = ord('A') if c.isupper() else ord('a')
            c = chr(((ord(c) + n) - Aa) % 26 + Aa)
        answer.append(c)
    
    return ''.join(answer)