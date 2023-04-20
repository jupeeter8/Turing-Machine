from graph import Graph
from collections import deque


# Finding if ther is a path between two nodes in an acyclic graph using
# DFS and BFS
def hasPathDFS(G: Graph, source: str, dest: str) -> bool:
    stack: list[str] = []
    stack.append(source)
    while stack:
        current_node = stack.pop()
        print(current_node, end=" ")
        if current_node == dest:
            return True
        for w in G.adj_list[current_node]:
            stack.append(w)
    return False


def hasPathBFS(G: Graph, source: str, dest: str) -> bool:
    queue = deque()
    queue.append(source)
    while queue:
        current_node = queue.popleft()
        print(current_node, end=" ")
        if current_node == dest:
            return True
        for w in G.adj_list[current_node]:
            queue.append(w)
    return False


nodes = ["f", "g", "h", "i", "j", "k"]
edges = [("f", "g"), ("f", "i"), ("g", "h"), ("i", "g"), ("i", "k"), ("j", "i")]

G = Graph(edges, nodes, directed=True)
print(G)
print(hasPathDFS(G, "f", "j"))
print(hasPathBFS(G, "f", "k"))
