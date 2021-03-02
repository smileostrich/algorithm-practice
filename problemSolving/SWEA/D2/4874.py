T = int(input())
for tc in range(1, T+1):
    stack = list(input().split())
    stack.reverse()
    tmp = []
    error = False
    while stack:
        cur = stack.pop()
        if cur.isdigit():
            tmp.append(int(cur))
        elif cur == '.':
            if error or len(tmp) >= 2:
                print(f'#{tc} error')
            else:
                print(f'#{tc}', tmp.pop())
            break
        else:
            if len(tmp) >= 2:
                if cur == '*':
                    tmp.append(tmp.pop() * tmp.pop())
                elif cur == '/':
                    fir = tmp.pop()
                    sec = tmp.pop()
                    tmp.append(sec // fir)
                elif cur == '+':
                    tmp.append(tmp.pop() + tmp.pop())
                else:
                    fir = tmp.pop()
                    sec = tmp.pop()
                    tmp.append(sec - fir)
            else:
                error = True