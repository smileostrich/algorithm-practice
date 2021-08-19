X = int(input())
s = 1
k = 1
while s <= X:
    s += k
    k += 1
s -= k
k-=1
if k % 2 == 0:
    print(str(X-s)+'/'+str(k-(X-s)+1))
else:
    print(str(k-(X-s)+1)+'/'+str(X - s))