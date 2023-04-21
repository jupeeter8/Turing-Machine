from collections import deque


def DFS(grid, source, visited, n, m):
    ci, cj = source
    if (ci, cj) in visited:
        return False

    visited.add((ci, cj))
    neighbours = [[ci + 1, cj], [ci - 1, cj], [ci, cj + 1], [ci, cj - 1]]
    for i in neighbours:
        ni, nj = i
        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == "L":
            DFS(grid, [ni, nj], visited, n, m)
    return True


def findIslands(grid):
    n = len(grid)
    m = len(grid[0])
    visited = set()
    islandCount = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "L":
                # Start DFS
                if DFS(grid, [i, j], visited, n, m):
                    islandCount += 1
                continue

    return islandCount


grid = [
    ["W", "L", "W", "W", "W"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "L", "W"],
    ["W", "W", "L", "L", "W"],
    ["L", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "W"],
]

print(findIslands(grid))


# stack = []
# stack.append([i, j])
# new_island = False
# while stack:
#     ci, cj = stack.pop()
#     if (ci, cj) not in visited and grid[ci][cj] == "L":
#         new_island = True
#         visited.add((ci, cj))
#         if ci + 1 < n:
#             stack.append([ci + 1, cj])
#         if ci - 1 >= 0:
#             stack.append([ci - 1, cj])
#         if cj + 1 < m:
#             stack.append([ci, cj + 1])
#         if cj - 1 >= 0:
#             stack.append([ci, cj - 1])
# islandCount += 1 if new_island else 0
