class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def nullify(i,j):
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            if i - 1 > -1:
                nullify(i-1,j)
            if i + 1 < len(grid):
                nullify(i+1,j)
            if j - 1 > -1:
                nullify(i,j - 1)
            if j + 1 < len(grid[0]):
                nullify(i,j + 1)
            return
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    nullify(i,j)

        return count