def back(start, depth):
    if depth == L:
        cnt = 0
        for i in range(C):
            if li_comb[i] and li_al[i] in li_ja:
                cnt += 1
        if cnt >= 1 and L-cnt >= 2:
            for i in range(C):
                if li_comb[i]:
                    print(li_al[i], end='')
            print()
        return
    for i in range(start, C):
        li_comb[i] = 1
        back(i+1, depth+1)
        li_comb[i] = 0

L, C = map(int, input().split())
li_al = list(input().split())
li_al.sort()
li_comb = [0] * C
li_ja = ['a','e','i','o','u']
back(0,0)