def solution(num_list):
    multi_sum = 1
    
    for n in num_list:
        multi_sum *= n
    
    return int(multi_sum < sum(num_list) ** 2)