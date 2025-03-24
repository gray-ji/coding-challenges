def solution(numLog):
    control_dic = { -1: 'w', 1: 's', -10: 'd', 10: 'a' }
    answer = ''
    
    for i in range(1, len(numLog)):
        answer += control_dic[numLog[i - 1] - numLog[i]]
        
    return answer