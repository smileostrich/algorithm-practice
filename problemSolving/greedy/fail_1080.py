from sys import stdin
import heapq

inp = lambda: stdin.readline().rstrip()

N, M = map(int, inp().split())
col = (N-3)+1
row = (M-3)+1
mat1 = [inp() for _ in range(N)]
mat2 = [inp() for _ in range(N)]

def same_chk(mat1, mat2):
    if mat1 == mat2:
        return True
    else:
        return False

def same_all(mat):
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 1:
                return False


if col <= 0 or row <= 0:
    if mat1 == mat2:
        print(0)
    else:
        print(-1)
else:
    chk_same = same_chk(mat1, mat2)

    new_mat = [[] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if mat1[i][j] == mat2[i][j]:
                new_mat[i].append(int(0))
            else:
                new_mat[i].append(int(1))
    li_dif = []
    for i in range(col):
        tmp_sum = 0
        for repeat_i in range(3):
            for j in range(row):
                for repeat_j in range(3):
                    tmp_sum += new_mat[i+repeat_i][j+repeat_j]
        heapq.heappush(li_dif, (-tmp_sum, i, j))
    print(li_dif)
    cnt_result = 0
    while not chk_same:
        print(heapq.heappop(li_dif))
        m_tmp_sum, x, y = heapq.heappop(li_dif)
        for i in range(x, x+3):
            for j in range(y,y+3):
                new_mat[i][j] = not new_mat[i][j]
        chk_same = same_all(new_mat)
        cnt_result += 1
    print(cnt_result)


