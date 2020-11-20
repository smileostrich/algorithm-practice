# 20분

from sys import stdin
import re


N = int(stdin.readline().rstrip())
result = []


for _ in range(N):
    contents = stdin.readline().rstrip()

    sample = re.findall(r'\d+', contents)
    result += list(map(int, sample))
result.sort()
for i in result:
    print(i)
# print('\n'.join(result))
