class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        selling_price = prices[0]

        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - selling_price)
            selling_price = min(selling_price, prices[i])

        return max_profit