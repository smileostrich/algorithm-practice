T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li_t = list(map(int, input().split()))
    li_t.sort()
    print(f'#{tc}', *li_t)