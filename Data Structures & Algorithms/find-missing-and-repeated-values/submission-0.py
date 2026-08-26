class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        hm = defaultdict(int)
        for i in range(n):
            for j in (grid[i]):
                hm[j] += 1
        
        res = []
        double = 0
        missing = 0
        for i in range(1,n*n+1):
            if hm[i] == 0:
                missing = i
            if hm[i] == 2:
                double = i
        return [double,missing]

