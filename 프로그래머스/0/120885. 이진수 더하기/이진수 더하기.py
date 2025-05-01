def solution(bin1, bin2):
    max_len = len(bin1) if len(bin1) >= len(bin2) else len(bin2)
    round_num = False
    answer = ''
    
    for i in range(1, max_len+1):
        n1 = '0' if len(bin1) < i else bin1[-i]
        n2 = '0' if len(bin2) < i else bin2[-i]
        
        if round_num:
            if n1 == '1' and n2 == '1':
                answer = '1' + answer
            elif n1 == '1' or n2 == '1':
                answer = '0' + answer
            else:
                answer = '1' + answer
                round_num = False
        else:
            if n1 == '1' and n2 == '1':
                answer = '0' + answer
                round_num = True
            elif n1 == '1' or n2 == '1':
                answer = '1' + answer
            else:
                answer = '0' + answer
    
    return '1' + answer if round_num else answer