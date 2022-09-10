class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf, minPrice = 0, prices[0]
        for price in prices[1:]:
            maxProf = max(maxProf, price - minPrice)
            minPrice = min(minPrice, price)
        return maxProf