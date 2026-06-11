class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for n in range(numRows):
            arr = [1]
            val = 1
            for k in range(1, n+1):
                val = ( val * (n-k+1) )// k
                arr.append(val)
            res.append(arr)
        return res




                