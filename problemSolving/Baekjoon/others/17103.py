T = int(input())
li_n = [int(input()) for _ in range(T)]
lar = max(li_n)+1
li_so = [True]*lar
li_so[0],li_so[1] = False, False
for i in range(2, int(lar**0.5)+1):
    if li_so[i] == True:
        for j in range(i+i, lar, i):
            li_so[j] = False
for i in li_n:
    cnt = 0
    for j in range(2, i//2+1):
        if li_so[j] and li_so[i-j]:
            cnt += 1
    print(cnt)