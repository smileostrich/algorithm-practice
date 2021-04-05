# 높이 지정
H = 4

# 1 2 1 3 2 4 2 5 3 6 3 7 4 8 4 9 5 10
tree = [-1]*(pow(2,H+1))
# data = [-1,'A','B','C','D','E','F','G','H','I','J']
# for i in range(1, len(data)):
data = [1, 2, 1, 3, 2, 4, 2, 5, 3, 6, 3, 7, 4, 8, 4, 9, 5, 10]
for i in range(0, len(data), 2):
    parent = data[i]
    child = parent
    p_idx = tree.index(parent)
    if tree[p_idx*2] == -1:
        tree[p_idx*2] = child
    else:
        tree[p_idx*2+1] = child
def pre_order(v)
