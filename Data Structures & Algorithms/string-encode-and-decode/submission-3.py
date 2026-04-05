class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[i] != "#":
                i+=1
            num = int(s[j:i])
            i+=1
            j = i
            j += num
            string = s[i:j]
            i = j
            res.append(string)
        return res
