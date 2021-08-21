N = int(input())
def recur(n):
    if n == 1:
        return 1
    return n*recur(n-1)
if N==0:
    print(1)
else:
    print(recur(N))