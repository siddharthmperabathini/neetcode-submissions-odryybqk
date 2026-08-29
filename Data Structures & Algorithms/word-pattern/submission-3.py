class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hm = defaultdict(str)
        arr = s.split(" ")
        if len(pattern) != len(arr):
            return False
        for i in range(len(pattern)):
            if hm[pattern[i]] == "" and hm[arr[i]] == "":
                hm[arr[i]] = pattern[i]
                hm[pattern[i]] = arr[i]
            elif hm[arr[i]] != pattern[i]:
                return False
        return True