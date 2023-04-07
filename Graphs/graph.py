class Graph:
    def __init__(self, pairList: list[tuple[int, int]]) -> None:
        self.adj_list = {int: list}

        for n1, n2 in pairList:
            if n1 not in self.adj_list:
                self.adj_list[n1] = []
            if n2 not in self.adj_list:
                self.adj_list[n2] = []

            self.adj_list[n1].append(n2)
            self.adj_list[n2].append(n1)
        self.v = len(self.adj_list) - 1

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


def DFS_stack(G: Graph, start: int, visited=None):
    if visited is None:
        visited: list[bool] = [False] * G.v


pair = [(1, 2), (2, 4), (2, 5), (4, 6), (3, 4), (6, 3)]
G = Graph(pair)
G.add_edge((5, 6))
print(G)
DFS(G, 1)
