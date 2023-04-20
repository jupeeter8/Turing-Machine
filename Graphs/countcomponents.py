from collections import deque
from graph import Graph


def countConnectedComponents(G: Graph):
    visited = set()
    count = 0
    for node in G.nodes:
        queue = deque()
        queue.append(node)
        new_comp = False
        while queue:
            curr_node = queue.popleft()
            if curr_node not in visited:
                new_comp = True
                visited.add(curr_node)
                for neighbour in G.adj_list[curr_node]:
                    queue.append(neighbour)
        count += 1 if new_comp else 0
    return count


nodes = [0, 1, 2, 3, 4, 5, 8]
egdes = [(1, 0), (0, 5), (0, 8), (8, 5), (4, 2), (2, 3), (4, 3)]
G = Graph(egdes, nodes)
print(countConnectedComponents(G))
