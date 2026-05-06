class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [0] * len(stones)
        
        for i in range(len(heap)):
            heap[i] = -stones[i]
        
        heapq.heapify(heap)
        while len(heap) > 1:
            biggest = -heapq.heappop(heap)
            second_biggest = -heapq.heappop(heap)
            if biggest > second_biggest:
                heapq.heappush(heap, -(biggest - second_biggest))
            elif biggest > second_biggest:
                heapq.heappush(heap, -(second_biggest - biggest))
        return -heap[0] if len(heap) > 0 else 0

        