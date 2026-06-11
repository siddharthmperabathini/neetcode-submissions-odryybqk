class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hs = set()
        l = 0
        for r in range(len(nums)):
            if r - l > k:
                hs.remove(nums[l])
                l += 1
            if nums[r] in hs:
                return True
            else:
                hs.add(nums[r])
        return False