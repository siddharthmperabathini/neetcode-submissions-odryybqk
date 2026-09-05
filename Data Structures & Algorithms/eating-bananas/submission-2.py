class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = 100000000000
        while l <= r:
            m = (l+r) // 2
            time = 0
            for num in piles:
                time += (num // m)
                if num % m:
                    time += 1
            
            if time <= h:
                r = m -1
                res = min(m,res)

            else:
                l = m + 1
        return res

