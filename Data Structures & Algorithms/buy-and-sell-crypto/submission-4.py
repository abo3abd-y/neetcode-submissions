class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        left = 0
        right = 1
        while left < len(prices) and right < len(prices):
            if prices[right] - prices[left] >= 0:
                max_profit = max(max_profit, prices[right] - prices[left])
                right += 1
            else:
                left += 1
                right = left + 1
            

        return max_profit