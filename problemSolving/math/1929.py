import sys


M, N = map(int, sys.stdin.readline().split())

prime_li = [2]

if M == 1:
    print(1)
    print(2)
elif M == 2:
    print(2)
for i in range(3, N+1):
    prime_check = True
    for tt in prime_li:
        if i % tt == 0:
            prime_check = False
            break
    if prime_check == True:
        prime_li.append(i)
        print(i)
    else:
        continue

print(prime_li)