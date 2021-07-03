def climbingLeaderboard(ranked, player):
    li_rank = list(set(ranked))
    li_rank.sort()
    size = len(li_rank)
    dic_rank = dict(zip(range(1,size+1),range(size,0,-1)))
    idx = 0
    result = []
    for score in player:
        flag = False
        while True:
            if flag:
                result.append(dic_rank[idx+1])
                break
            if li_rank[idx] == score:
                result.append(dic_rank[idx+1])
                break
            elif li_rank[idx] < score:
                if idx+1 < size:
                    idx += 1
                else:
                    flag = True
            elif li_rank[idx] > score:
                if idx > 0:
                    idx -= 1
                    result.append(dic_rank[idx+1])
                else:
                    result.append(dic_rank[idx+1]+1)
                break
    return result

print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10],[5, 25, 50, 120]))
# print(climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]))