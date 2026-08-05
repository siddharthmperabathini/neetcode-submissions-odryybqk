class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hs = set()
        dup = set()
        for num in arr:
            if num not in hs and num not in dup:
                hs.add(num)
            else:
                if num in hs:
                    hs.remove(num)
                    dup.add(num)
        for string in arr:
            if string in hs:
                k -= 1
                if k == 0:
                    return string
        return ""