def gcd(a,b):
    while b > 0:
        a,b = b, a%b
    return a


N = int(input())
li_ring = list(map(int, input().split()))
for i in range(1, len(li_ring)):
    gc = gcd(li_ring[0],li_ring[i])
    print(str(li_ring[0]//gc)+'/'+str(li_ring[i]//gc))

