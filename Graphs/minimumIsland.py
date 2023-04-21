from sys import maxsize


def DFS(
    grid: list[list[int]],
    source: list[int],
    visited: set[int, int],
    n: int,
    m: int,
    size=0,
) -> int:
    ci, cj = source
    if (ci, cj) in visited:
        return 0
    rowInbound = 0 <= ci < n
    colInbounnd = 0 <= cj < m
    if not rowInbound or not colInbounnd:
        return 0
    if grid[ci][cj] == "W":
        return 0
    visited.add((ci, cj))
    size = 1
    size += DFS(grid, [ci + 1, cj], visited, n, m)
    size += DFS(grid, [ci - 1, cj], visited, n, m)
    size += DFS(grid, [ci, cj + 1], visited, n, m)
    size += DFS(grid, [ci, cj - 1], visited, n, m)
    return size


def minimumIsland(grid):
    n = len(grid)
    m = len(grid[0])
    visited = set()
    minIsland = maxsize
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "L":
                if (a := DFS(grid, [i, j], visited, n, m)) > 0:
                    minIsland = min(a, minIsland)

    return minIsland if minIsland < maxsize else 0


grid = [
    ["W", "L", "W", "W", "W"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "L", "W"],
    ["W", "W", "L", "L", "W"],
    ["L", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "W"],
]

print(minimumIsland(grid))
