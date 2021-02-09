T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    h_li = 0
    s_li = 0
    for p in range(M):
        h_li += li[p]
        s_li += li[p]
    for i in range(1, N-M+1, 1):
        t_sum = 0
        for p in range(M):
            t_sum += li[i+p]
        if t_sum > h_li:
            h_li = t_sum
        elif t_sum < s_li:
            s_li = t_sum
    print(f'#{test_case} {h_li-s_li}')


    # N, L = 7, 3
    # arr = [1, 2, 3, 7, 5, 4, 3]
    #
    # # 덱 생성
    # dq = deque()
    #
    # for i in range(N):
    #     while dq and dq[-1][1] > arr[i]:
    #         dq.pop()
    #     dq.append((i, arr[i]))  # 튜플 형태로 저장 : (인덱스, 수(값))
    #
    #     while dq and dq[0][0] < i - L + 1:
    #         dq.popleft()
    #
    #     # 범위내의 최솟값 출력
    #     print(dq[0][1], end=" ")
    # #
    # # print(f'#{test_case} {high} {-1*v1}')