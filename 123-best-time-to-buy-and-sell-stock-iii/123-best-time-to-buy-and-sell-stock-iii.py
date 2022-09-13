class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if not n:   return 0
        
        gain_1, gain_2 = 0, 0
        min_p1, min_p2 = prices[0], prices[0]
        
        for i in range(1, n):
            min_p1 = min(min_p1, prices[i])
            gain_1 = max(gain_1, prices[i] - min_p1)
            
            min_p2 = min(min_p2, prices[i] - gain_1)
            gain_2 = max(gain_2, prices[i] - min_p2)

        return gain_2