# concept

# from sys import stdin
# from itertools import permutations
#
# inp = lambda: stdin.readline().rstrip()
#
# cnt_bu = int(inp())
# li_bu = list(map(str, inp().split()))
# li_num = [0,1,2,3,4,5,6,7,8,9]
#
# li_perfect = []
#
# for sn in li_num:
#     for p in range(cnt_bu+1):
#         li_num[sn]
#
# li_permu = permutations(li_num, cnt_bu+1)
# result = [li_permu[0],li_permu[-1]]
# for k in result:
#     li_tmp = []
#     for i in range(cnt_bu):
#         li_tmp.append(str(k[i]))
#         li_tmp.append(li_bu[i])
#     li_tmp.append(str(k[-1]))
#     tmp = ''.join(li_tmp)
#     if bool(eval(tmp)):
#         li_perfect.append(li_tmp)
# print(''.join(li_perfect[-1][::2]))
# print(''.join(li_perfect[0][::2]))

# from sys import stdin
# from itertools import permutations
#
#
# inp = lambda: stdin.readline().rstrip()
#
# K = int(inp())
# li_bu = list(map(str, inp().split()))
# li_n = list(range(0,10))
# small = li_n[0:K+1]
# big = li_n[-1:10-(K+2):-1]
#
# li_small = list(permutations(small, K+1))
# li_big = list(permutations(big, K+1))
#
# c_samll = 0
# c_big = 0
#
# for cur in li_small:
#     li_tmp = []
#     for i in range(K):
#         li_tmp.append(str(cur[i]))
#         li_tmp.append(li_bu[i])
#     li_tmp.append(str(cur[-1]))
#     re_tmp = ''.join(li_tmp)
#     if eval(re_tmp):
#         break
#     c_samll += 1
#
# for cur in li_big:
#     li_tmp = []
#     for i in range(K):
#         li_tmp.append(str(cur[i]))
#         li_tmp.append(li_bu[i])
#     li_tmp.append(str(cur[-1]))
#     re_tmp = ''.join(li_tmp)
#     if eval(re_tmp):
#         break
#     c_big += 1
# print(''.join(map(str, li_big[c_big])))
# print(''.join(map(str, li_small[c_samll])))


# 백준
def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1

    a[i-1],a[j] = a[j],a[i-1]

    j = len(a)-1
    while i < j:
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1

    return True

def prev_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] <= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] >= a[i-1]:
        j -= 1

    a[i-1],a[j] = a[j],a[i-1]

    j = len(a)-1
    while i < j:
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1

    return True

def check(perm, a):
    for i in range(len(a)):
        if a[i] == '<' and perm[i] > perm[i+1]:
            return False
        if a[i] == '>' and perm[i] < perm[i+1]:
            return False
    return True

k = int(input())
a = input().split()
small = [i for i in range(k+1)]
big = [9-i for i in range(k+1)]

while True:
    if check(small,a):
        break
    if not next_permutation(small):
        break
while True:
    if check(big, a):
        break
    if not prev_permutation(big):
        break

print(''.join(map(str,big)))
print(''.join(map(str,small)))
