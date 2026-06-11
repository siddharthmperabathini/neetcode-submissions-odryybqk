class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0 
        slow = 0
        fast = 0 
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                k += 1
                nums[slow + 1] = nums[fast]
                slow += 1
            fast += 1
        return k + 1