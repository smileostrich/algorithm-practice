N = int(input())
li_n = []
for i in range(N):
    li_n.append(tuple(map(int, input().split())))

li_n.sort(key=lambda x:(x[1],x[0]))
for i1,i2 in li_n:
    print(f'{i1} {i2}')