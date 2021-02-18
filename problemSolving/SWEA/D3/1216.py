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
            while cur <= cur_in and cur_in <= 99:
                for j in range((cur_in-cur)//2):
                    if tmp[cur+j] != tmp[cur_in-j]:
                        break
                else:
                    tmp_hi = cur_in-cur+1
                    if highest < tmp_hi:
                        highest = tmp_hi
                cur_in += 1
            cur += 1
    print(f'#{tc} {highest}')
    # for i in range(100):
    #     tmp = input()
    #     li_mat.append(tmp)
    #
    #     cur = 0
    #     while cur <= 98:
    #         cur_in = 1
    #         while cur < cur_in and cur_in <= 99:
    #             for j in range((cur_in-cur)//2):
    #                 if tmp[cur+j] != tmp[cur_in-j]:
    #                     break
    #             else:
    #                 tmp_hi = cur_in-cur+1
    #                 if highest < tmp_hi:
    #                     highest = tmp_hi
    #             cur_in += 1
    #         cur += 1
    # for k in range(100):
    #     cur = 0
    #     while cur <= 98:
    #         cur_in = 1
    #         while cur < cur_in and cur_in <= 99:
    #             for j in range((cur_in - cur) // 2):
    #                 if li_mat[cur + j][k] != li_mat[cur_in - j][k]:
    #                     break
    #             else:
    #                 tmp_hi = cur_in - cur + 1
    #                 if highest < tmp_hi:
    #                     highest = tmp_hi
    #             cur_in += 1
    #         cur += 1

    # print(f'#{tc} {highest}')
