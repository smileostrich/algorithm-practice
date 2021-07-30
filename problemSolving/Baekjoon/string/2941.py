s=input()
set_temp = {"c=":0,"c-":0,"dz=":0,"d-":0,"lj":0,"nj":0,"s=":0,"z=":0}
cnt = 0
cnt_result = 0
while cnt < len(s):
    if cnt < len(s)-2:
        cur = s[cnt:cnt + 2]
        cur2 = s[cnt:cnt + 3]
        if cur2 in set_temp:
            # set_result.add(cur2)
            cnt += len(cur2)
        elif cur in set_temp:
            # set_result.add(cur)
            cnt += len(cur)
        else:
            # set_result.add(s[cnt])
            cnt += 1
    elif cnt < len(s)-1:
        cur = s[cnt:cnt + 2]
        if cur in set_temp:
            # set_result.add(cur)
            cnt += len(cur)
        else:
            # set_result.add(s[cnt])
            cnt += 1
    else:
        # set_result.add(s[cnt])
        cnt += 1
    cnt_result += 1
print(cnt_result)
