def solution(numbers, direction):
    if direction == 'right':
        return [numbers[len(numbers)-1]] + numbers[:len(numbers)-1]
    return numbers[1:len(numbers)] + [numbers[0]]