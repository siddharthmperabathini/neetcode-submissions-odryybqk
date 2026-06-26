class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def nullify(i,j):
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            area = 1
            if i - 1 > -1:
                area += nullify(i-1,j)
            if i + 1 < len(grid):
                area += nullify(i+1,j)
            if j - 1 > -1:
                area += nullify(i,j - 1)
            if j + 1 < len(grid[0]):
                area += nullify(i,j + 1)
            return area
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res,nullify(i,j))

        return res