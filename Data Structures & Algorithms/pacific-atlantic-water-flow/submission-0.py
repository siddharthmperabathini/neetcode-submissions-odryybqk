class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        pacific = set()
        atlantic = set()
        def dfs(i, j, prev, visit):
            if (i,j) in visit or i == len(heights) or i == -1 or j == len(heights[0]) or j == -1 or heights[i][j] < prev:
                return
            visit.add((i,j))
            dfs(i+1,j,heights[i][j],visit)
            dfs(i-1,j,heights[i][j],visit)
            dfs(i,j+1,heights[i][j],visit)
            dfs(i,j-1,heights[i][j],visit)
        rows = len(heights)
        cols = len(heights[0])
        for i in range(len(heights)):
            dfs(i,0,heights[i][0], pacific)
            dfs(i,cols - 1, heights[i][cols-1],atlantic )
        for j in range(len(heights[0])):
            dfs(0,j,heights[0][j],pacific)
            dfs(rows - 1, j,heights[rows- 1][j],atlantic)
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res

        
