class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]
        for i in range(len(nums)):
            l = i
            r = len(nums) 
            while l < r:
                m = (l+r) // 2
                if (prefix[m + 1] - prefix[i]) < target:
                    l = m + 1
                else:
                    res = min(res, (m - i + 1))
                    r = m 
        return res if res != float('inf') else 0
