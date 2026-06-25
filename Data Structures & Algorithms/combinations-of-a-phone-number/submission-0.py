class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        cur = ""
        hm = {
            "1": "def",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def dfs(pos):
            nonlocal cur
            if pos == len(digits):
                res.append(cur)
                return
            for char in hm[digits[pos]]:
                cur += char
                dfs(pos + 1)
                cur = cur[:-1]
        if digits == "":
            return []
        dfs(0)
        return res
