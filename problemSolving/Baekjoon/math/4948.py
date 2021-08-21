k = 300000
li_primes = [False,False]+[True]*k
for i in range(2,int(k**0.5)+1):
    if li_primes[i]:
        for j in range(2*i,k+1,i):
            li_primes[j] = False
while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(n+1,2*n+1):
        if li_primes[i]:
            cnt += 1
    print(cnt)