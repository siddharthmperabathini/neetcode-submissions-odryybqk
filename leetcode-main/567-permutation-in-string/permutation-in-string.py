class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counts1 = [0] * 26
        for char in s1:
            counts1[ord(char) - ord('a')] += 1
        counts2 = [0] * 26
        for i in range(len(s1)):
            counts2[ord(s2[i]) - ord('a')] += 1
        matches = 0
        for i in range (0,26):
            if counts1[i] == counts2[i]:
                matches += 1
        l = 0
        r = len(s1) - 1
        while r < (len(s2) - 1):
            if matches == 26:
                return True
            index = ord(s2[l]) - ord('a')
            was_match = (counts2[index] == counts1[index])
            counts2[index] -= 1
            if counts2[index] == counts1[index]:
                matches += 1
            elif was_match and counts2[index] != counts1[index]:
                matches -= 1
            l += 1

            index = ord(s2[r + 1]) - ord('a')
            was_match = (counts2[index] == counts1[index])
            counts2[index] += 1
            if counts2[index] == counts1[index]:
                matches += 1
            elif was_match and counts2[index] != counts1[index]:
                matches -= 1
            r += 1
        return matches == 26




            

        
