class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hm = defaultdict(int)
        for num in nums:
            hm[num] +=1
        for item,key in hm.items():
            if key % 2 == 1:
                return False
        return True
        