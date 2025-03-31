def solution(myStr):
    myStr = myStr.replace('b', 'a').replace('c', 'a').split('a')
    answer = [s for s in myStr if s != '']
    
    return answer if answer else ['EMPTY']