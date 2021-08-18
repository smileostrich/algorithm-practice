from collections import Counter

N = input()
li = list(N)
li.sort(reverse=True)
print(''.join(li))


# for i in range(N,-1, -1):
#     result += i