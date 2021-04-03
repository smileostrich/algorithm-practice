from collections import deque

def solution(gift_cards, wants):
    dic_cur = {}
    cnt = 0
    for i in range(len(gift_cards)):
        if gift_cards[i] != wants[i]:
            if gift_cards[i] in dic_cur:
                dic_cur[gift_cards[i]].append(i)
            else:
                dic_cur[gift_cards[i]] = deque([i])
        else:
            cnt += 1

    for idx, val in dic_cur.items():
        t_cnt = 0
        while val and t_cnt <= len(val):
            cur = val.popleft()
            if wants[cur] in dic_cur and dic_cur[wants[cur]]:
                cnt += 1
                if idx != wants[dic_cur[wants[cur]][0]]:
                    # val.append(dic_cur[wants[cur]][0])
                    dic_cur[idx].append(dic_cur[wants[cur]][0])
                else:
                    cnt += 1
            else:
                t_cnt += 1
                dic_cur[idx].append(cur)

    return len(gift_cards) - cnt



print(solution([4, 5, 3, 2, 1], [2, 4, 4, 5, 1]))
print(solution(	[5, 4, 5, 4, 5], [1, 2, 3, 5, 4]))