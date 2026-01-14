def solution(survey, choices):
    scores = {'R':0, 'T':0,
             'C':0, 'F':0,
             'J':0, 'M':0,
             'A':0, 'N':0}
    
    for choice, char in zip(choices, survey):
        if choice:
            key = char[0] if choice < 4 else char[1]
            score = abs(choice - 4)
            scores[key] += score
    
    answer = 'R' if scores['R'] >= scores['T'] else 'T'
    answer += 'C' if scores['C'] >= scores['F'] else 'F'
    answer += 'J' if scores['J'] >= scores['M'] else 'M'
    answer += 'A' if scores['A'] >= scores['N'] else 'N'
    
    return answer