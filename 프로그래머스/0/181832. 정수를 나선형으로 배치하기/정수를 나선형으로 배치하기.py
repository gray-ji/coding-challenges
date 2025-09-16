def solution(n):
    answer = [[0] * n for _ in range(n)]
	
    top, bottom, left, right = 0, n-1, 0, n-1
    num = 1
    
    while num <= n*n:
        for j in range(left, right+1):
            answer[top][j] = num
            num += 1
        top += 1
        
        for i in range(top, bottom+1):
            answer[i][right] = num
            num += 1
        right -= 1
        
        for j in range(right, left-1, -1):
            answer[bottom][j] = num
            num += 1
        bottom -= 1
        
        for i in range(bottom, top-1, -1):
            answer[i][left] = num
            num += 1
        left += 1
    
    return answer