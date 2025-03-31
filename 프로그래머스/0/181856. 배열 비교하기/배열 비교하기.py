def solution(arr1, arr2):
    size1, size2 = len(arr1), len(arr2)
    
    if size1 == size2:
        sum1, sum2 = sum(arr1), sum(arr2)
        
        if sum1 == sum2:
            return 0
        return 1 if sum1 > sum2 else -1
    
    return 1 if size1 > size2 else -1