class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        count = 0
        while count < len(word1) and count < len(word2):
            s+= word1[count]
            s+= word2[count]
            count += 1
        if count < len(word1):
            s+= word1[count::]
        if count < len(word2):
            s+= word2[count::]
        return s
        