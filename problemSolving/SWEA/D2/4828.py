T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    li = list(map(int, input().split()))
    highest = li[0]
    smallest = li[0]
    for i in li:
        if i > highest:
            highest = i
            continue
        if i < smallest:
            smallest = i
    print(f'#{test_case} {highest-smallest}')