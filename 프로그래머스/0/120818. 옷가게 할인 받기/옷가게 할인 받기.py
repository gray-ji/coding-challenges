def solution(price):
    if price >= 100000:
        if price < 300000:
            price *= 0.95
        elif price < 500000:
            price *= 0.9
        else:
            price *= 0.8
    
    return int(price)