def solution(myString, pat):
    idx = myString.rfind(pat) + len(pat)
    return myString[:idx]