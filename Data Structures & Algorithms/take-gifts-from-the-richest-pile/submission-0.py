import math, heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts_heaped = gifts
        for i in range(len(gifts_heaped)):
            gifts_heaped[i] = -gifts[i]
        heapq.heapify(gifts_heaped)

        for _ in range(k):
            popped = -heapq.heappop(gifts_heaped)
            heapq.heappush(gifts_heaped, -math.floor(popped**0.5))
        return sum(-x for x in gifts_heaped)