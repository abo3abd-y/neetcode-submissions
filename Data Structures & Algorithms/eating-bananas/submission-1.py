class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        left, right = 1, max_pile
        result = 0
        # time complexity is O(n * log(max_piles))
        while left <= right:
            mid = (left + right) // 2
            hours = sum(math.ceil(pile/mid) for pile in piles)
            print(mid)
            if hours <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result