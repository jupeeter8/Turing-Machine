from graph import Graph
import sys
from collections import deque


def shortestPath(G: Graph, source: int, dest: int) -> None:
    """
    Implementation of shortest path algorithms using BFS

    """
    visited = dict.fromkeys(list(G.adj_list.keys()), False)
    distance = dict.fromkeys(list(G.adj_list.keys()), sys.maxsize)
    previous = dict.fromkeys(list(G.adj_list.keys()), -1)

    distance[source] = 0
    queue = deque()
    queue.append(source)
    while queue:
        node = queue.popleft()
        dist = distance[node] + 1
        visited[node] = True
        for w in G.adj_list[node]:
            if dist < distance[w]:
                distance[w] = dist
                previous[w] = node
            if not visited[w]:
                queue.append(w)
    node = previous[dest]
    path = [dest, node]
    while node > 0:
        node = previous[node]
        if node > 0:
            path.append(node)
    return distance[dest], reversed(path)


nodes = [1, 2, 3, 4, 5, 6, 7]
edges = [(1, 3), (1, 2), (2, 3), (2, 4), (2, 7), (3, 4), (3, 5), (4, 5), (5, 6)]

G = Graph(edges, nodes)
print(G)
distance, path = shortestPath(G, 2, 5)
print(f"Distance = {distance}\nPath: {list(path)}")
