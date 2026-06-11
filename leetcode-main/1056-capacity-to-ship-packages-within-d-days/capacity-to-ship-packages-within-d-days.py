class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = 0
        def calc(mid):
            left = mid
            days = 1
            for w in weights:
                if left - w < 0:
                    days += 1
                    left = mid

                left -= w
            return days
                

        while l <= r:
            mid = (l + r) // 2
            time = 0
            cur_weight = 0
            time = calc(mid)

            if time > days:
                l = mid + 1
            else:
                res = mid
                r = mid - 1
        return res
