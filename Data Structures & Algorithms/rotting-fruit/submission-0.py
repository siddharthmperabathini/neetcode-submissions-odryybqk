class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        print(fresh)
        while q and fresh > 0:
            for i in range(len(q)):
                x, y = q.popleft()
                if x + 1 < len(grid) and grid[x + 1][y] != 0 and grid[x + 1][y] != 2:
                    q.append((x + 1, y))
                    grid[x+1][y] = 2
                    fresh -= 1
                if x - 1 >= 0 and grid[x - 1][y] != 0 and grid[x - 1][y] != 2:
                    q.append((x - 1, y))
                    grid[x-1][y] = 2
                    fresh -= 1
                if y + 1 < len(grid[0]) and grid[x][y + 1] != 0 and grid[x][y + 1] != 2:
                    q.append((x, y + 1))
                    grid[x][y+1] = 2
                    fresh -= 1
                if y - 1 >= 0 and grid[x][y - 1] != 0 and grid[x][y - 1] != 2:
                    q.append((x, y - 1))
                    grid[x][y-1] = 2
                    fresh -= 1
            time += 1
        print(time)
        print(fresh)

        return time if fresh == 0 else -1
