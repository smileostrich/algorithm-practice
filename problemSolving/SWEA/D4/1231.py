def inorder(idx):
    global result

    if li_tree[idx] == -1:
        return
    inorder(2*idx)
    result += li_tree[idx]
    inorder(2*idx+1)
    return


for tc in range(1, 11):
    n = int(input())
    i = 0
    while True:
        if pow(2, i) <= n:
            i += 1
        else:
            break
    height = pow(2, i+1)+1
    li_tree = [-1]*(height)
    for i in range(1,n+1):
        li_tree[i] = list(input().split())[1]

    result = ''

    inorder(1)

    print(f'#{tc} {result}')