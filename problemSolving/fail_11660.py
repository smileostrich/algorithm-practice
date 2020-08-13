import sys

N = list(map(int, sys.stdin.readline().split()))
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N[0])]
M = [list(map(int, sys.stdin.readline().split())) for _ in range(N[1])]
count = 0
for idxi, i in enumerate(M):
    for idxj, j in enumerate(i):
        M[idxi][idxj] = j-1

# for i in range(M[0][0], M[0][2]+1):
#     for j in range(M[0][1], M[0][3]+1):
#         count += matrix[M[i][j+1]][M[i][j+1]]

for k in range(N[1]):
    for i in range(M[k][0], M[k][2]+1):
        for j in range(M[k][1], M[k][3]+1):
            # print(i, j)
            # print(M[i][j], M[i][j])
            # print(M[i][j+1], M[i][j+1])
            count += matrix[M[i][j]][M[i][j]]
            print(matrix[M[i][j]][M[i][j]])
            # count += matrix[M[j-1][0]][M[j-1][1]]
            # count += matrix[M[j-1][2]][M[j-1][3]]


# joh
print(matrix)
print(M)
print(count)
# print(M[0][0:2])
# print(M[0][2:4])

# matrix[0][0:2]
# matrix[0][2:4]
# matrixM[0][0:2]

# print(matrix[M[0][0]][M[0][1]])
# print(matrix[M[0][2]][M[0][3]])
# print(count)