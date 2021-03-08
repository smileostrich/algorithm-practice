# 20분
def rets(size, li):
    size_li = len(li)
    cnt = 0
    while True:
        if size <= cnt * size_li:
            break
        else:
            cnt += 1
    if cnt == 0:
        return 1
    return cnt


def solution(answers):
    answer = []
    n1 = [1, 2, 3, 4, 5]
    n2 = [2, 1, 2, 3, 2, 4, 2, 5]
    n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    size = len(answers)
    c1 = n1 * rets(size, n1)
    c2 = n2 * rets(size, n2)
    c3 = n3 * rets(size, n3)
    a1 = 0
    a2 = 0
    a3 = 0
    for i in range(size):
        if answers[i] == c1[i]:
            a1 += 1
        if answers[i] == c2[i]:
            a2 += 1
        if answers[i] == c3[i]:
            a3 += 1
    highest = max(a1, a2, a3)
    if a1 == highest:
        answer.append(1)
    if a2 == highest:
        answer.append(2)
    if a3 == highest:
        answer.append(3)

    return answer