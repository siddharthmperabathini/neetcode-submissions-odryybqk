class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        hm = {0:n, 1:n}
        res = []
        cur = ""
        def dfs():
            nonlocal cur
            if len(cur) == n * 2:
                res.append(cur)
                return
            if hm[1] > hm[0]:
                cur += ")"
                hm[1] -= 1
                dfs()
                hm[1] += 1
                cur = cur[:-1]
            if hm[0] != 0:
                cur += "("
                hm[0] -= 1
                dfs()
                hm[0] += 1
                cur = cur[:-1]
        dfs()
        return res