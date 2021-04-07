T = 10
for test_case in range(1, T + 1):
    N = int(input())
    dic_c = {}
    li_tree = [-1 for _ in range(N + 1)]
    for i in range(N):
        li_tmp = list(input().split())
        if len(li_tmp) == 4:
            node, op, c1, c2 = li_tmp
            node, c1, c2 = int(node), int(c1), int(c2)
            dic_c[node] = (c1,c2)
            li_tree[node] = op
        else:
            node, value = li_tmp
            node, value = int(node), int(value)
            li_tree[node] = value
    for i in sorted(dic_c.keys(), reverse=True):
        if li_tree[i] == '+':
            li_tree[i] = li_tree[dic_c[i][0]] + li_tree[dic_c[i][1]]
        elif li_tree[i] == '-':
            li_tree[i] = li_tree[dic_c[i][0]] - li_tree[dic_c[i][1]]
        elif li_tree[i] == '*':
            li_tree[i] = li_tree[dic_c[i][0]] * li_tree[dic_c[i][1]]
        elif li_tree[i] == '/':
            li_tree[i] = li_tree[dic_c[i][0]] // li_tree[dic_c[i][1]]
    print(f'#{test_case} {int(li_tree[1])}')