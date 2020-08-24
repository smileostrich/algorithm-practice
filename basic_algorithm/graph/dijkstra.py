import sys


class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex tDistance from Source")
        for node in range(self.V):
            print(node, "t", dist[node])

    def minDistance(self, dist, sptSet):
        min = sys.maxsize

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and \
                        sptSet[v] == False and \
                        dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijkstra(0)





# using linked list
# class Graph(object):
#     def __init__(self):
#         self.nodes = set()
#         self.edges = {}
#         self.distances = {}
#
#     def add_node(self, value):
#         self.nodes.add(value)
#
#     def add_edge(self, from_node, to_node, distance):
#         self._add_edge(from_node, to_node, distance)
#         self._add_edge(to_node, from_node, distance)
#
#     def _add_edge(self, from_node, to_node, distance):
#         self.edges.setdefault(from_node, [])
#         self.edges[from_node].append(to_node)
#         self.distances[(from_node, to_node)] = distance
#
#
# def dijkstra(graph, initial_node):
#     visited = {initial_node: 0}
#     current_node = initial_node
#     path = {}
#
#     nodes = set(graph.nodes)
#
#     while nodes:
#         min_node = None
#         for node in nodes:
#             if node in visited:
#                 if min_node is None:
#                     min_node = node
#                 elif visited[node] < visited[min_node]:
#                     min_node = node
#
#         if min_node is None:
#             break
#
#         nodes.remove(min_node)
#         cur_wt = visited[min_node]
#
#         for edge in graph.edges[min_node]:
#             wt = cur_wt + graph.distances[(min_node, edge)]
#             if edge not in visited or wt < visited[edge]:
#                 visited[edge] = wt
#                 path[edge] = min_node
#
#     return visited, path
#
#
# def shortest_path(graph, initial_node, goal_node):
#     distances, paths = dijkstra(graph, initial_node)
#     route = [goal_node]
#
#     while goal_node != initial_node:
#         route.append(paths[goal_node])
#         goal_node = paths[goal_node]
#
#     route.reverse()
#     return route
#
#
# if __name__ == '__main__':
#     g = Graph()
#     g.nodes = set(range(1, 7))
#     g.add_edge(1, 2, 7)
#     g.add_edge(1, 3, 9)
#     g.add_edge(1, 6, 14)
#     g.add_edge(2, 3, 10)
#     g.add_edge(2, 4, 15)
#     g.add_edge(3, 4, 11)
#     g.add_edge(3, 6, 2)
#     g.add_edge(4, 5, 6)
#     g.add_edge(5, 6, 9)
#     assert shortest_path(g, 1, 5) == [1, 3, 6, 5]
#     assert shortest_path(g, 5, 1) == [5, 6, 3, 1]
#     assert shortest_path(g, 2, 5) == [2, 3, 6, 5]
#     assert shortest_path(g, 1, 4) == [1, 3, 4]