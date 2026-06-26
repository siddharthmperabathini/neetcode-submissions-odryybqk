class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(i,j):
            if i == -1 or i == len(grid) or j == -1 or j == len(grid[0]) or grid[i][j] == 0:
                return 1
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            p = dfs(i+1,j)
            p += dfs(i-1,j)
            p += dfs(i, j+1)
            p += dfs(i,j-1)
            return p
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i,j)
        return 0
        
            
        
