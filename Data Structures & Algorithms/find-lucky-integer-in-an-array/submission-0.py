class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hm = defaultdict(int)
        for num in arr:
            hm[num] += 1
        res = -1
        for i,v in hm.items():
            if i == v:
                res = max(i,res)
        return res