from collections import deque


def solution(li_bal):
    t = (li_bal, 0)
    dq = deque([])
    dq.append(t)
    set_result = set()
    while dq:
        li_q, flag = dq.popleft()
        if len(li_q) == 1:
            set_result.add(li_q[0])
        else:
            for i in range(len(li_q)-1):
                if li_q[i] > li_q[i+1]:
                    tmp = li_q[:i]
                    tmp.extend(li_q[i+1:])
                    dq.append((tmp, 0))
                    if not flag:
                        tmp2 = li_q[:i+1]
                        if i+2 < len(li_q):
                            tmp2.extend(li_q[i + 2:])
                            dq.append((tmp2, 1))
                        else:
                            dq.append((tmp2, 1))
                else:
                    tmp2 = li_q[:i+1]
                    if i + 2 < len(li_q):
                        tmp2.extend(li_q[i + 2:])
                        dq.append((tmp2, 0))
                    else:
                        dq.append((tmp2, 0))
                    if not flag:
                        tmp = li_q[:i]
                        tmp.extend(li_q[i + 1:])
                        dq.append((tmp, 1))
    return len(set_result)

print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))