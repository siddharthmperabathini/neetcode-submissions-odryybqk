class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            real_num = abs(num)
            index = real_num - 1
            if nums[index] < 0:
                return real_num
            else:
                nums[index] *= -1
        