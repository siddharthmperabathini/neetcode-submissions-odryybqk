class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = 10000
        while l <= r:
            mid = (l+r) //2
            if nums[l] < nums[r]:
                res = min(res,nums[l])
            res = min(res, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return res
        
        