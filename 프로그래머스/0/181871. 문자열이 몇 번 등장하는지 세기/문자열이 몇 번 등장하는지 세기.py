def solution(myString, pat):
    answer = 0
    
    for i, v in enumerate(myString):
        if v == pat[0] and myString[i:].startswith(pat):
            answer += 1
        
    return answer