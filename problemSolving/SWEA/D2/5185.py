T = int(input())
for test_case in range(1, T + 1):
    N, he = input().split()
    val = bin(int('0x'+he,0))[2:]
    val = val.zfill((int(N)*4))
    print(f"#{test_case} {val}")