def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    
    i = 2
    while i <= numer or i <= denom:
        if numer % i == 0 and denom % i == 0:
            numer //= i
            denom //= i
        else:
            i += 1
    
    return [numer, denom]