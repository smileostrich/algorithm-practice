def solution(student, k):
    cnt = 0
    for i in range(0,len(student)):
        s_cnt = 0
        cur = i
        while cur < len(student):
            if student[cur] == 1:
                s_cnt += 1
                if s_cnt == k:
                    cnt += 1
                elif s_cnt > k:
                    break
            elif s_cnt == k:
                cnt += 1
            cur += 1
    return cnt




print(solution([0, 1, 0], 2))