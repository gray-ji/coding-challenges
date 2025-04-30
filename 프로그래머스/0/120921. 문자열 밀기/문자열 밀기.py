def solution(A, B):
    answer = 0
    
    for i in range(len(A) + 1):
        if A == B:
            break
            
        if i == len(A):
            answer = -1
        else:
            A = A[-1] + A[:-1]
            answer += 1
    
    return answer