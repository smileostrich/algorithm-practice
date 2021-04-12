dic_code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    code = ''
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                code += arr[i][j - 55: j + 1]
    decode = []
    s, e = 0, 7
    for _ in range(8):
        decode.append(dic_code[code[s:e]])
        s += 7
        e += 7

    if ((decode[0] + decode[2] + decode[4] + decode[6]) * 3 + decode[1] + decode[3] + decode[5] + decode[7]) % 10 == 0:
        print(f'#{tc} {sum(decode)}')
    else:
        print(f'#{tc} 0')