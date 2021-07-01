def solution(progresses, speeds):
    size = len(progresses)
    days = []
    for i in range(size):
        last = (100-progresses[i]) // speeds[i]
        if (100-progresses[i]) % speeds[i]:
            last += 1
        days.append(last)
    answer = []
    count = 1
    for i in range(1, len(days)):
        if days[i - count] >= days[i]:
            count += 1
        else:
            answer.append(count)
            count = 1
    answer.append(count)
    return answer



print(solution([99, 1, 99, 1], [1, 1, 1, 1]))