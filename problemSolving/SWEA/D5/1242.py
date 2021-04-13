dic_decode = {'112':0, '122':1, '221':2,'114':3, '231':4,'132':5, '411':6, '213':7, '312':8, '211':9}
dic_bin = {'0':'0000', '1':'0001', '2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}


def examine(arr):
    if ((arr[7]+arr[5]+arr[3]+arr[1])*3 + arr[0]+arr[2]+arr[4]+arr[6]) % 10:
        return False
    return True

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li_code = [input()[:M] for _ in range(N)]
    for n in range(N):
        bin = ''
        for char in li_code[n]:
            bin += dic_bin[char]
        li_code[n] = bin
    res = []
    visited = []
    ans = 0
    for n in range(N):
        n1, n2, n3 = 0, 0, 0
        if '1' not in li_code[n]:
            continue
        for m in range(M*4-1,-1,-1):
            if n2 == 0 and n3 == 0 and li_code[n][m] =='1':
                n1 += 1
            elif n1 and n3 == 0 and li_code[n][m] == '0':
                n2 += 1
            elif n1 and n2 and li_code[n][m] == '1':
                n3 += 1
            elif n3 and li_code[n][m] == '0':
                mul = min(n1, n2, n3)
                res.append(dic_decode[str(n1//mul)+str(n2//mul)+str(n3//mul)])
                n1 = n2 = n3 = 0
                if len(res) == 8:
                    if res not in visited:
                        if examine(res):
                            ans += sum(res)
                        visited.append(res)
                    res = []
    print(f'#{tc} {ans}')