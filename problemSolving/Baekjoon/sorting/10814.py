N = int(input())
li_n = []
for i in range(N):
    age, name = input().split()
    li_n.append(tuple((int(age), i, name)))

li_n.sort(key=lambda x:(x[0],x[1]))
for a,i,n in li_n:
    print(f'{a} {n}')