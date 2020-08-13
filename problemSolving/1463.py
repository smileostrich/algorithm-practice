# dp
import sys

N = int(sys.stdin.readline())
li = [0] * (N+1)


def cal_3(i):
    return li[i//3] + 1


def cal_2(i):
    return li[i // 2] + 1


for i in range(2, N+1):
    if i%3 == 0 and i%2 == 0:
        li[i] = min(cal_3(i), cal_2(i), li[i-1] + 1)
    elif i%3 == 0:
        li[i] = min(cal_3(i), li[i-1] + 1)
    elif i%2 == 0:
        li[i] = min(cal_2(i), li[i-1] + 1)
    else:
        li[i] = li[i-1] + 1

print(li[N])

# 다른 사람들은 어떻게 짰는지 비교해보기
# n = int(input())
# d = [0]*(n+1)
# d[1] = 0
# for i in range(2, n+1):
#     d[i] = d[i-1] + 1
#     if i%2 == 0 and d[i] > d[i//2] + 1:
#         d[i] = d[i//2] + 1
#     if i%3 == 0 and d[i] > d[i//3] + 1:
#         d[i] = d[i//3] + 1
# print(d[n])






# def min(x, y):
#     return x if x <= y else y
#
#
# x = int(input())
#
# minimum_count = [0 for _ in range(x + 1)]
#
# index = 0
# while (True):
#     if index > x:
#         break
#
#     if index <= 1:
#         minimum_count[index] = 0
#     else:
#         temp_min = x + 1
#         if index % 3 == 0:
#             temp_index = int(index / 3)
#             temp_min = min(temp_min, minimum_count[temp_index])
#
#         if index % 2 == 0:
#             temp_index = int(index / 2)
#             temp_min = min(temp_min, minimum_count[temp_index])
#
#         temp_min = min(temp_min, minimum_count[index - 1])
#         minimum_count[index] = int(temp_min + 1)
#     index = index + 1
#
# print(minimum_count[x])



# Bottom-Up(For문 이용)
n = int(input())
d = [0]*(n+1)
d[1] = 0
for i in range(2, n+1):
    d[i] = d[i-1] + 1
    if i%2 == 0 and d[i] > d[i//2] + 1:
        d[i] = d[i//2] + 1
    if i%3 == 0 and d[i] > d[i//3] + 1:
        d[i] = d[i//3] + 1
print(d[n])


# Top Bottom (not DP)
# X = int(input())
# count = 0
# result = [X]
# def calculation(x):
#     lst = []
#     for i in x:
#         lst.append(i-1)
#         if i%3 ==0:
#             lst.append(i/3)
#         if i%2 ==0:
#             lst.append(i/2)
#     lst = set(lst)
#     lst = list(lst)
#     return lst
# while True:
#     if X == 1:
#         break
#     temp = result
#     result = []
#     result = calculation(temp)
#     count += 1
#     if min(result) == 1:
#         break
# print(count)