A,B,C = map(int, input().split())
if B >= C:
    print(-1)
else:
    cnt = 1
    ca,cb,cc = A,B,C
    tmp = ca//(cc-cb)
    cnt += tmp
    cb += B*tmp
    cc += C*tmp
    while ca+cb >= cc:
        cb += B
        cc += C
        cnt += 1
    print(cnt)