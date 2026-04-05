class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        res = 0
        for num in nums:
            if num + 1 not in hs:
                curr = num
                seq = 0
                while curr in hs:
                    seq += 1
                    
                    curr -= 1
                res = max(res,seq)
        return res
                