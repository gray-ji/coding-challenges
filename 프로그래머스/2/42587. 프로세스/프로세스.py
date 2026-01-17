from collections import deque

def solution(priorities, location):
    que = deque([(i, v) for i, v in enumerate(priorities)])
    priorities.sort()
    result = 1
    
    while True:
        i, v = que.popleft()
        if v == priorities[-1]:
            if i == location:
                return result
            priorities.pop()
            result += 1
        else:
            que.append((i, v))