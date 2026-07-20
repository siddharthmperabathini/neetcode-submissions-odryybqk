class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl = set()
        pac = set()
        rows = len(heights)
        cols = len(heights[0])
        def dfs(visited, i,j, prev):
            if (i,j) in visited or i == rows or i == -1 or j == cols or j == -1 or heights[i][j] < prev:
                return
            visited.add((i,j))
            dfs(visited, i+1,j, heights[i][j])
            dfs(visited, i-1,j, heights[i][j])
            dfs(visited, i,j+1, heights[i][j])
            dfs(visited, i,j-1, heights[i][j])
        for i in range(rows):
            dfs(pac,i,0,heights[i][0])
            dfs(atl,i,cols -1 ,heights[i][cols - 1])
        for j in range(cols):
            dfs(pac,0,j,heights[0][j])
            dfs(atl,rows-1,j ,heights[rows-1][j])
        res = []
        for item in pac:
            if item in atl:
                i,j = item
                res.append([i,j])
        return res


            
        