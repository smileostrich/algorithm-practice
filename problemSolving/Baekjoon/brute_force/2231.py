N = int(input())
for i in range(N):
    if N == i + sum(map(int, list(str(i)))):
        print(i)
        break
else:
    print(0)