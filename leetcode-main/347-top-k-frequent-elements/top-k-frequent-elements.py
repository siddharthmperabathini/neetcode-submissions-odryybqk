class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        for num in nums:
            hm[num] += 1
        temp = [[] for i in range(len(nums) + 1)]
        for num, freq in hm.items():
            temp[freq].append(num)
        res = []
        index = len(temp) - 1
        while len(res) < k:
            for num in temp[index]:
                res.append(num)
            index -=1
        return res

