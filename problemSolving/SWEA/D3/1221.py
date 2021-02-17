T = int(input())
for _ in range(T):
    tc, size = input().split()
    dic_st = {"ZRO":0, "ONE":0, "TWO":0, "THR":0, "FOR":0, "FIV":0, "SIX":0, "SVN":0, "EGT":0, "NIN":0}
    li_st = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    li_re = []
    for i in list(map(str, input().split())):
        dic_st[i] += 1
    for idx, val in dic_st.items():
        if val != 0:
            li_re.append(idx)
    print(f'{tc}')
    for j in li_re:
        for _ in range(dic_st[j]):
            print(j, end=' ')
    print()
