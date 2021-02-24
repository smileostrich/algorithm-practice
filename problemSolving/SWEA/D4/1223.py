op = {'*':1, '+':0}
for tc in range(1,11):
    N = int(input())
    st = input()
    stack = []
    post = ''
    for i in st:
        if i.isdigit():
            post += i
        else:
            while stack and (op[i] <= op[stack[-1]]):
                post += stack.pop()
            stack.append(i)
    while stack:
        post += stack.pop()
    for j in post:
        if j.isdigit():
            stack.append(j)
        elif j == '*':
            o1 = stack.pop()
            o2 = stack.pop()
            stack.append(int(o1)*int(o2))
        else:
            o1 = stack.pop()
            o2 = stack.pop()
            stack.append(int(o1)+int(o2))
    print(f'#{tc}', *stack)
