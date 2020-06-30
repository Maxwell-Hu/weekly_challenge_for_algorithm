class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: return 0
        minPrice = prices[0]
        maxProfit = 0
        for price in prices:
            maxProfit = max(price-minPrice, maxProfit)
            minPrice = min(minPrice, price)
        return maxProfit
