N = int(input())
result = []
while N != 1:
    for i in range(2,1000000000):
        if N%i == 0:
            N//=i
            result.append(i)
            break
for i in result:
    print(i)