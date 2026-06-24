class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        hm = defaultdict(int)
        res = []
        perm = []
        for num in nums:
            hm[num] += 1
        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
            for n in hm:
                if hm[n] > 0:
                    perm.append(n)
                    hm[n] -= 1
                    dfs()
                    hm[n] += 1
                    perm.pop()
        dfs()
        return res
