from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 1
    l_idx = bridge_length-1
    truck_weights = list(reversed(truck_weights))
    li_bridge = deque([0 for _ in range(bridge_length)])
    li_bridge[-1] = truck_weights.pop()
    remain_w = weight-li_bridge[-1]
    while li_bridge:
        remain_w += li_bridge.popleft()
        time += 1
        if truck_weights:
            cur = truck_weights.pop()
            if remain_w - cur >= 0:
                remain_w -= cur
                li_bridge.append(cur)
                l_idx = bridge_length-1
            else:
                li_bridge.append(0)
                truck_weights.append(cur)
                l_idx -= 1
        else:
            if l_idx == 0:
                return time
            else:
                l_idx -= 1


print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))