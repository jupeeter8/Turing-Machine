from collections import deque


class Graph:
    def __init__(
        self, edges: list[tuple[int, int]], nodes: list[int], directed=False
    ) -> None:
        self.adj_list: dict[int, list] = {}
        self.nodes = nodes
        if not directed:
            for n1, n2 in edges:
                if n1 not in self.adj_list:
                    self.adj_list[n1] = []
                if n2 not in self.adj_list and n2 is not None:
                    self.adj_list[n2] = []

                self.adj_list[n1].append(n2) if n2 is not None else None
                self.adj_list[n2].append(n1) if n2 is not None else None
        if directed:
            for n1, n2 in edges:
                if n1 not in self.adj_list:
                    self.adj_list[n1] = []
                if n2 not in self.adj_list:
                    self.adj_list[n2] = []

                self.adj_list[n1].append(n2)
        self.v = len(nodes)

    def add_edge(self, edge: tuple[int, int]) -> None:
        n1, n2 = edge
        if n1 not in self.adj_list:
            self.adj_list[n1] = []
        if n2 not in self.adj_list:
            self.adj_list[n2] = []

        self.adj_list[n1].append(n2)
        self.adj_list[n2].append(n1)

    def __str__(self) -> str:
        result = []
        for key in self.adj_list.keys():
            result.append(f"{key} -> {self.adj_list[key]}")
        return "\n".join(result)


def DFS(G: Graph, start: int, visited=None):
    if visited is None:
        visited: list[bool] = [False] * G.v
    while not all(visited):
        if visited[start - 1] == True:
            return
        visited[start - 1] = True
        print(start, end=" ")
        for w in G.adj_list[start]:
            if not visited[w - 1]:
                DFS(G, w, visited)
    return None


def DFS_stack(G: Graph, start: int) -> None:
    visited: list[bool] = [False] * G.v
    stack: list[int] = []
    stack.append(start)
    while stack:
        node = stack.pop()
        if not visited[node - 1]:
            visited[node - 1] = True
            print(node, end=" ")
            for w in G.adj_list[node]:
                stack.append(w)


def BFS(G: Graph, v: int) -> None:
    visited = dict.fromkeys(list(G.adj_list.keys()), False)
    queue = deque()

    queue.append(v)
    while queue:
        node = queue.popleft()
        if not visited[node]:
            visited[node] = True
            print(node, end=" ")
            for w in G.adj_list[node]:
                if not visited[w]:
                    queue.append(w)
    return None


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (4, 5), (2, 4)]
    G = Graph(edges, nodes)
    print(G)
    DFS(G, 1)
    print()
    DFS_stack(G, 1)
    print()
    BFS(G, 1)
