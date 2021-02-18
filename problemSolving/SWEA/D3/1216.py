# 32분 tmp
for _ in range(10):
    tc = int(input())
    li_mat = []
    highest = 1
    for i in range(100):
        tmp = input()
        li_mat.append(tmp)

        cur = 0
        while cur <= 98:
            cur_in = 1
            while cur_in <= 99:
                for i in range(cur_in//2):
                    if cur+i != cur_in-i:
                        break
                else:
                    tmp_hi = cur_in-cur
                    if highest < tmp_hi:
                        highest = tmp_hi
                cur_in += 1
            cur += 1
    print(f'#{tc} ')