# 10분
def solution(participant, completion):
    test = {}
    for i in participant:
        if i in test:
            test[i] += 1
        else:
            test[i] = 1
    for i in completion:
        test[i] -= 1
    for i,v in test.items():
        if v > 0:
            return i