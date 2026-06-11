class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        curr = 0 
        for char in s:
            res += abs(ord(char) - curr)
            curr = ord(char)
        return res - ord(s[0])