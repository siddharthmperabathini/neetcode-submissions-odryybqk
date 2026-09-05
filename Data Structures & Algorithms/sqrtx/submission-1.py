class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        l = 1
        r = x//2
        best = 0
        while l <= r:
            m = (l+r)//2
            if m * m <= x:
                best = max(best,m)
                l =m+1
            else:
                r = m-1
        return best