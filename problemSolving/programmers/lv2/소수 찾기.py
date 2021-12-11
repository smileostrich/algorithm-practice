from itertools import permutations

def solution(numbers):
    li_n = list(numbers)
    li_n.sort(reverse=True)
    highest = int(''.join(li_n))
    so = [True for _ in range(highest+1)]
    result = []
    so[0] = False
    so[1] = False
    for i in range(2, int(highest ** 0.5) + 1):
        if so[i]:
            for j in range(2 * i, highest + 1, i):
                so[j] = False
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            tmp = ''.join(j)
            if tmp[0] != '0':
                if so[int(tmp)]:
                    result.append(int(tmp))
    return result


print(solution("17"))