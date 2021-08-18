li_matrix = [list(map(int, input().split())) for _ in range(9)]
li_zeros = []
for i in range(9):
    for j in range(9):
        if li_matrix[i][j] == 0:
            li_zeros.append((i,j))
dic_d = {1:[0,1,2],2:[0,1,2],3:[0,1,2], 4:[3,4,5],5:[3,4,5],6:[3,4,5], 7:[6,7,8],8:[6,7,8],9:[6,7,8]}
def is_promising(y,x):
    dic_promising = { 1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0 }
    for i in range(9):
        if li_matrix[y][i] in dic_promising:
            dic_promising.pop(li_matrix[y][i])
        if li_matrix[i][x] in dic_promising:
            dic_promising.pop(li_matrix[i][x])
    for i in dic_d[y+1]:
        for j in dic_d[x+1]:
            if li_matrix[i][j] in dic_promising:
                dic_promising.pop(li_matrix[i][j])
    return dic_promising.keys()

flag = False
def dfs(idx):
    global flag
    if flag:
        return
    if idx == len(li_zeros):
        for i in li_matrix:
            print(*i)
        flag = True
        return 0
    y, x = li_zeros[idx]
    promising = is_promising(y,x)
    for n in promising:
        li_matrix[y][x] = n
        dfs(idx+1)
        li_matrix[y][x] = 0
dfs(0)