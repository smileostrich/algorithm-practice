import math


T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    print(math.factorial(m)//(math.factorial(m-n)*math.factorial(n)))