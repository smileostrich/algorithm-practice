Y, X = map(int, input().split())
li_matrix = [list(input()) for _ in range(Y)]
li_cmpa = []
li_cmpb = []
for _ in range(4):
    li_cmpa.append(list('WBWBWBWB'))
    li_cmpa.append(list('BWBWBWBW'))
    li_cmpb.append(list('BWBWBWBW'))
    li_cmpb.append(list('WBWBWBWB'))
lo = 99999
for y in range(Y-8+1):
    for x in range(X-8+1):
        cnta = 0
        cntb = 0
        for c_y in range(8):
            for c_x in range(8):
                if li_cmpa[c_y][c_x] != li_matrix[y+c_y][x+c_x]:
                    cnta += 1
                if li_cmpb[c_y][c_x] != li_matrix[y+c_y][x+c_x]:
                    cntb += 1
        lo = min(lo,cnta,cntb)
print(lo)