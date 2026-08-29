class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp = [0] * 101
        for h in heights:
            temp[h] += 1
        expected = []
        for i in range(len(temp)):
            for j in range(temp[i]):
                expected.append(i)
        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1
        return res
