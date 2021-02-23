import re
from collections import deque

T = int(input())
for tc in range(1, T+1):
    line = input()
    new_line = deque(re.findall("[{}()]", line))
    stack = []
    result = 1
    while new_line:
        cur = new_line.popleft()
        if cur == '{':
            stack.append(cur)
        elif cur == '(':
            stack.append(cur)
        elif cur == '}':
            if not stack:
                result = 0
                break
            tmp = stack.pop()
            if tmp != '{':
                result = 0
                break
        elif cur == ')':
            if not stack:
                result = 0
                break
            tmp = stack.pop()
            if tmp != '(':
                result = 0
                break
    if stack:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {result}')