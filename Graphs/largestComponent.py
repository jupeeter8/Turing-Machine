from graph import Graph
from collections import deque


def largestComponent(G: Graph):
    visited = set()
    largetsSize = 0
    for node in G.nodes:
        stack: list[int] = []
        stack.append(node)
        size = 0
        while stack:
            curr_node = stack.pop()
            if curr_node not in visited:
                visited.add(curr_node)
                size += 1
                for neighbour in G.adj_list[curr_node]:
                    stack.append(neighbour)
        largetsSize = max(size, largetsSize)
    return largetsSize


nodes = [0, 1, 2, 3, 4, 5, 8, 7, 6]
edges = [(1, 0), (0, 5), (0, 8), (8, 5), (4, 2), (2, 3), (4, 3), (3, 7), (2, 6)]
G = Graph(edges, nodes)
print(G)
print(largestComponent(G))
