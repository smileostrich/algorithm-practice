# 시간초과 fail
# 다시풀어보기







# 인터넷+수정

# import re
# from itertools import permutations
#
# def solution(expression):
#     #1
#     op = [x for x in ['*','+','-'] if x in expression]
#     op = [list(y) for y in permutations(op)]
#     ex = re.split(r'(\D)',expression)
#
#     #2
#     a = []
#     for x in op:
#         _ex = ex.copy()
#         for y in x:
#             while y in _ex:
#                 tmp = _ex.index(y)
#                 _ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1]))
#                 _ex = _ex[:tmp]+_ex[tmp+2:]
#         a.append(abs(int(_ex[-1])))
#
#     #3
#     return max(a)

# print(solution("100-200*300-500+20"))

# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin
from itertools import combinations

num_attr = int(stdin.readline().rstrip())
num_thre = float(stdin.readline().rstrip())
num_rows = int(stdin.readline().rstrip())

dict_cnt = {}
for _ in range(num_rows):
    result = list(combinations(list(map(str, stdin.readline().rstrip().split(','))), num_attr))
    for test in result:
        if test in dict_cnt:
            dict_cnt[test] += 1
        else:
            dict_cnt[test] = 1

for k,v in dict_cnt.items():
    if num_thre <= (v / num_rows):
        print(f'{",".join(list(k))}')