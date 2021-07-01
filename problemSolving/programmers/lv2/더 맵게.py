import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while True:
        for i in scoville:
            if i < K:
                if len(scoville) < 2:
                    return -1
                cnt += 1
                h1, h2 = heapq.heappop(scoville), heapq.heappop(scoville)
                heapq.heappush(scoville,h1 + (h2*2))
                break
        else:
            break
    return cnt

print(solution([1, 2, 3, 9, 10, 12], 7))