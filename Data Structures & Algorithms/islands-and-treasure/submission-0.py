class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        INF = 2147483647
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i,j))
        while queue:
            x,y = queue.popleft()
            if x + 1 < len(grid) and grid[x+1][y] == INF:
                grid[x+1][y] = grid[x][y] + 1 if grid[x][y] != INF else 1
                queue.append((x+1,y))
            if x - 1 >= 0 and grid[x-1][y] == INF:
                grid[x-1][y] = grid[x][y] + 1 if grid[x][y] != INF else 1
                queue.append((x-1,y))
            if y+ 1 < len(grid[0]) and grid[x][y+ 1] == INF:
                grid[x][y+1] = grid[x][y] + 1 if grid[x][y] != INF else 1
                queue.append((x,y+1))
            if y- 1 >= 0 and grid[x][y-1] == INF:
                grid[x][y-1] = grid[x][y] + 1 if grid[x][y] != INF else 1
                queue.append((x,y - 1))
            