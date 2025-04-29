def solution(numbers):
    alphabet = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4',
                'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    answer = ''
    
    while numbers != '':
        if numbers[:3] in alphabet:
            answer += alphabet[numbers[:3]]
            numbers = numbers[3:]
        elif numbers[:4] in alphabet:
            answer += alphabet[numbers[:4]]
            numbers = numbers[4:]
        else:
            answer += alphabet[numbers[:5]]
            numbers = numbers[5:]
    
    return int(answer)