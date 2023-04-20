from graph import Graph
from collections import deque


def hasPathUndirected(G: Graph, source: str, dest: str, visited: any = None):
    if visited is None:
        visited = dict().fromkeys(list(G.adj_list.keys()), False)
    if source == dest:
        return True
    elif not visited[source]:
        visited[source] = True
        for w in G.adj_list[source]:
            if hasPathUndirected(G, w, dest, visited):
                return True
    return False


nodes = [1, 2, 3, 4, 5, 6, 7, 8]
egdes = [(1, 2), (3, None), (4, 6), (5, 6), (6, 8), (7, 6)]
G = Graph(egdes, nodes)
print(G)
# print(hasPathUndirected(G, "l", "j"))
