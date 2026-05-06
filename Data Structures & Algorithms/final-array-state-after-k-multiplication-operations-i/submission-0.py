class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = nums
        for i in range(len(heap)) : 
            heap[i] = (heap[i], i)
        heapq.heapify(heap)
        for i in range(k):
            popped = heapq.heappop(heap)
            heapq.heappush(heap, ((popped[0] * multiplier),popped[1] ))
        
        heap.sort(key=lambda x : x[1])
        heap =  [value for value,_ in heap]
        return heap
