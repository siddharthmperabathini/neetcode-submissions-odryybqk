class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = 100000000
        while l <=r :
            m = (l+r) //2
            count = 1
            remain = m
            for num in weights:
                if remain < num:
                    count += 1
                    remain = m
                remain -= num
            if count <= days:
                r = m -1
                res = m
            else:
                l = m + 1
        return res

            

                
