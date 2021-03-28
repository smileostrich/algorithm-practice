N, K = map(int, input().split())

result = 0
if N < 2:
    print(0)
else:
    for i in range(2, N+1):
        result = (result+K) % i
    print(result+1)