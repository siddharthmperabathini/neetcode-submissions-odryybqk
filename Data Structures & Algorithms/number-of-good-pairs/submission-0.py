class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hm = defaultdict(int)
        res = 0
        for num in nums:
            res += hm[num]
            hm[num] += 1
        return res
