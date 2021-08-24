N = int(input())
li_so = [True]*(N+1)
li_so[0] = False
li_so[1] = False
for i in range(2, int(N**0.5)+1):
    if li_so[i]:
        for j in range(2*i,N+1,i):
            li_so[j] = False
li_primes = [i for i in range(2,N+1) if li_so[i] == True]
left, right = 0,0
tsum = 0
cnt = 0
while True:
    if tsum >= N:
        if tsum == N:
            cnt += 1
        tsum -= li_primes[left]
        left += 1
    elif right==len(li_primes):
        break
    else:
        tsum += li_primes[right]
        right += 1
print(cnt)