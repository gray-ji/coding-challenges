def solution(myString):
    answer = [v for v in myString.split('x') if v != '']
    return sorted(answer)