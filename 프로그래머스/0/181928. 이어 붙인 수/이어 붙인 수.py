def solution(num_list):
    merged_list = ['', '']
    
    for n in num_list:
        merged_list[n % 2] += str(n)
    
    return int(merged_list[0]) + int(merged_list[1])