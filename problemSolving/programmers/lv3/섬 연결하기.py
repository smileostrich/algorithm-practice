def solution(n, costs):
    # 크루스칼
    result = 0
    costs.sort(key=lambda x: x[2])
    visited = set([costs[0][0]])
    while len(visited) != n:
        for i, li_tmp in enumerate(costs):
            if li_tmp[0] in visited and li_tmp[1] in visited:
                continue
            if li_tmp[0] in visited or li_tmp[1] in visited:
                visited.update((li_tmp[0], li_tmp[1]))
                result += li_tmp[2]
                costs[i] = [-1, -1, -1]
                break
    return result

print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))