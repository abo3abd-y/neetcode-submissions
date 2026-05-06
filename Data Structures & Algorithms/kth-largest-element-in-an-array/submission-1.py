class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-val for val in nums]
        return -heapq.nsmallest(k, heap)[-1]

