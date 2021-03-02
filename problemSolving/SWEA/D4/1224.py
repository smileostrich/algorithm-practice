isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}

for test_case in range(1, 11):
    N = int(input())
    data = []
    calc = []
    for d in input():
        if d.isdigit():
            data.append(d)
        elif d == ')':
            while data[-1] != '(':
                data.append(calc.pop())
            data.pop()
        else:
            while calc and not icp[d] > isp[calc[-1]]:
                data.append(calc.pop())
            calc.append(d)
    while calc:
        data.append(calc.pop())

    stack = []
    for d in data:
        if d.isdigit():
            stack.append(int(d))
        elif d == '+':
            stack.append(stack.pop() + stack.pop())
        elif d == '*':
            stack.append(stack.pop() * stack.pop())
    print('#{} {}'.format(test_case, stack[0]))