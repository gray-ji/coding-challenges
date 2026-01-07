def solution(s):
    alpha = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4',
             'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    answer = []
    temp = []
    
    for v in s:
        if v.isalpha():
            temp.append(v)
        else:
            answer.append(v)
            
        key = ''.join(temp)
        if key in alpha:
            answer.append(alpha[key])
            temp.clear()
        
    return int(''.join(answer))