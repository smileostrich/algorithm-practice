N = int(input())
li_n = []
for i in range(N):
    tmp = input()
    li_n.append(tuple((len(tmp), tmp)))

li_n.sort(key=lambda x:(x[0],x[1]))
result = dict()
for i1,i2 in li_n:
    if i2 in result:
        continue
    else:
        result[i2] = 1
for i in result.keys():
    print(i)