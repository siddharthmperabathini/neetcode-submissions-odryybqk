class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] = gifts[i] * -1
        heapq.heapify(gifts)
        for i in range(k):
            temp = heapq.heappop(gifts)
            temp *= -1
            temp = floor(sqrt(temp))
            temp *= -1
            heapq.heappush(gifts,temp)
        return sum(gifts) * -1
