# 32분 tmp
for _ in range(10):
    tc = int(input())
    li_mat = []
    highest = 1
    for i in range(100):
        tmp = input()
        li_mat.append(tmp)
        for size in range(0,99):
            cur = 0
            while cur <= 100-size:
                for j in range(size//2):
                    if tmp[cur+j] != tmp[cur+size-1-j]:
                        break
                else:
                    if highest < size:
                        highest = size
                cur += 1
    for k in range(100):
        for size in range(0,99):
            cur = 0
            while cur <= 100-size:
                for j in range(size//2):
                    if li_mat[cur+j][k] != li_mat[cur+size-1-j][k]:
                        break
                else:
                    if highest < size:
                        highest = size
                cur += 1
    print(f'#{tc} {highest}')
