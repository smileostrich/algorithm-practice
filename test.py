import unittest


print([1,2,3]*3)


li = {(3,4):None,(1,2):(3,4)}
def test(li, a, b, c):
    tmp = li[(a, b)]
    c += 1
    if tmp != None:
        return test(li, *tmp, c)
    else:
        return c

print(test(li, 1,2,3))


# test = ['12345']
# print(test[0][1])


# li = [1,2,3]
# for i in range(5):
#     for j in range(5):
#         if j == 5 and i == 4:
#             break
#         print(j)

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# from functools import reduce
#
# primes = [2, 3, 5, 7, 11, 13]
#
# def product(*numbers):
#     p = reduce(lambda x, y: x * y, numbers)
#     return p
# print(product(*primes));print(product(primes))

# for i in range(5, 0, -1):
#     print(i)

# print([0,0] + [1])
# print([0,0] + [1]*(3-1))

# test = {1:3,2:4}
# print(test.popitem())
# print(test.keys())

# current = 0
# for _ in range(0, 10):
#     current += 1

# print(current)
# def quicksort(x):
#     if len(x) <= 1:
#         return x
#
#     pivot = x[len(x) // 2]
#     less = []
#     more = []
#     equal = []
#     for a in x:
#         if a < pivot:
#             less.append(a)
#         elif a > pivot:
#             more.append(a)
#         else:
#             equal.append(a)
#
#     return quicksort(less) + equal + quicksort(more)
#
#
# list = [8, 13, 2, 6, 1, 4]
# quicksort(list)
#         # list = [8, 1, 2, 5, 10, 14, 7, 21]
#         # self.assertEqual([1, 2, 5, 7, 8, 10, 14, 21], quicksort(list)