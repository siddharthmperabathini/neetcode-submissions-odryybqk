class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(string):
            l = 0
            r = len(string) -1
            while l < r:
                if string[l] != string[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        res = []
        cur = []
        def dfs(i):
            if i == len(s):
                res.append(cur.copy())
                return
            for j in range(i,len(s)):
                if isPalindrome(s[i:j+1]):
                    cur.append(s[i:j+1])
                    dfs(j+1)
                    cur.pop()
        dfs(0)
        return res

        