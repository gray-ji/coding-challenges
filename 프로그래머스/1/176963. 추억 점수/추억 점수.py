def solution(name, yearning, photo):
    score = dict(zip(name, yearning))
    return [sum([score.get(per, 0) for per in pic]) for pic in photo]