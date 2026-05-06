class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-val for val in nums]
        return -heapq.nsmallest(k, nums)[-1]

