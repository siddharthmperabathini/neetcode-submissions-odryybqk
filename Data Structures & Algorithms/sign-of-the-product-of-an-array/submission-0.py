class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        if 0 in nums:
            return 0
        for num in nums:
            res *= num
        if res > 0:
            return 1
        else:
            return -1