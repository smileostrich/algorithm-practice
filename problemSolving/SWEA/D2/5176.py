T = int(input())

def inorder(node):
    global N
    global cnt
    if node < N+1:
        inorder(2*node)
        li_tree[node] = cnt
        cnt += 1
        inorder(2*node+1)


for test_case in range(1, T + 1):
    N = int(input())
    li_tree = [-1 for i in range(N+1)]
    cnt = 1
    inorder(1)
    result = ''
    print(f'#{test_case} {li_tree[1]} {li_tree[N//2]}')