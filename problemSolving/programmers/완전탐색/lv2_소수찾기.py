# 21분
from itertools import permutations


def so(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, num//2+1):
        if num % i == 0:
            return False
    else:
        return True


def solution(numbers):
    li_ans = []
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            tmp = ''.join(j)
            if tmp[0] != '0':
                if so(int(tmp)):
                    li_ans.append(int(tmp))
    return len(set(li_ans))