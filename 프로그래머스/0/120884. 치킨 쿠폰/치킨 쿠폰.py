def solution(chicken):
    coupon = chicken
    answer = 0
    
    while coupon > 9:
        answer += 1
        coupon -= 9
    
    return answer