class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        hold, sold, rest = -inf, 0, 0
        
        for price in prices:
            prev_sold, prev_hold, prev_rest = sold, hold, rest
            
            rest = max(prev_sold, prev_rest)
            sold = max(prev_hold + price, prev_sold)
            hold = max(prev_rest - price, prev_hold)
            
        return max(sold, rest)