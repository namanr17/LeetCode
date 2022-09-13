class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache(None)
        def trade(day, hold):
            if day >= len(prices):  return 0
            
            if hold:
                return max(prices[day] + trade(day+2, False), trade(day+1, True))
            else:   return max(-prices[day] + trade(day+1, True), trade(day+1, False))
        
        return trade(0, False)