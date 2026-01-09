def solution(n, arr1, arr2):
    answer = []

    for a1, a2 in zip(arr1, arr2):
        line = str(bin(a1 | a2))[2:].replace('1', '#').replace('0', ' ')
        answer.append((' ' * (n - len(line))) + line)

    return answer