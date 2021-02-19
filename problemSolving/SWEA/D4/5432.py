T = int(input())
for tc in range(1, T+1):
    li_in = list(input())
    stack = []
    cnt = 0
    cur = 0
    for i in range(len(li_in)):
        stack.append(li_in[i])
        if li_in[i] == '(':
            cnt += 1
            cur += 1
        else:
            if stack[i-1] == '(':
                cur -= 1
                cnt -= 1
                cnt += cur
            else:
                cur -= 1
    print(f'{tc} {cnt}')