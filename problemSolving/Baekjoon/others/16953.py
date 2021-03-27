from collections import deque

A, B = map(int, input().split())

queue = deque([(1,A)])
result = -1
while queue:
    idx, value = queue.popleft()
    if value == B:
        result = idx
        break
    elif value <= B:
        if value * 2 <= B:
            queue.append((idx+1, value*2))
        queue.append((idx+1, value*10+1))
    else:
        continue
print(result)