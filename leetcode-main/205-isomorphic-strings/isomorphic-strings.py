class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hmS = defaultdict(str)
        hmT = defaultdict(str)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            if (s_char in hmS and hmS[s_char] != t_char) or (t_char in hmT and hmT[t_char] != s_char):
                return False
            hmS[s_char] = t_char
            hmT[t_char] = s_char
        return True