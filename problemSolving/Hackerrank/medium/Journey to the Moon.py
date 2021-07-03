from collections import defaultdict


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        v = stack.pop()
        visited.add(v)
        stack.extend(graph[v] - visited)
    return visited


def journeyToMoon(n, ast_pairs):
    graph = defaultdict(set)
    print(graph)
    asts = set()
    for a1, a2 in ast_pairs:
        graph[a1].add(a2)
        graph[a2].add(a1)
        asts.add(a1)
        asts.add(a2)

    iso_asts = set([i for i in range(n)]) - asts

    groups = []
    while asts:
        ast = asts.pop()
        connected_asts = dfs(graph, ast)
        groups.append(connected_asts)
        # 한번 방문한 팀은 다시 방문하지 않는다.
        asts = asts - connected_asts

    for i in iso_asts:
        groups.append({i})

    # 뒤에 추가된 것들을 따로 분리해야 한다. 그래야 추가된 녀석들이 만드는
    # 패턴을 알 수 있다.
    # A*B + A*C + B*C -- A*B + A*C + B*C -- A*B + (A+B)*C
    # A*B + A*C + A*D + B*C + B*D + C*D
    # - A*B + (A+B)*C (A+B+C)*D
    # A*B + A*C + A*D + A*E + B*C + B*D + B*E + C*D + C*E + D*E
    # - A*B + (A+B)*C + (A+B+C)*D + (A+B+C+D)*E
    idx1, idx2 = 0, 1
    group_sum = 0
    tmp_sum = 0
    while idx1 < len(groups):
        group_sum += tmp_sum * len(groups[idx1])
        tmp_sum += len(groups[idx1])

        # group_sum += tmp_sum*(len(groups[idx1 + 1]))
        idx1 += 1

    return group_sum


n, p = list(map(int, input().strip().split(' ')))
ast_pairs = []
for _ in range(p):
    astronaut = [int(a) for a in input().strip().split(' ')]
    ast_pairs.append(astronaut)

# result = journeyToMoon(n, ast_pairs)
# print(result)


print(journeyToMoon(5, [[0, 1], [2, 3], [0, 4]]))
# print(journeyToMoon(4,[[0, 2]]))