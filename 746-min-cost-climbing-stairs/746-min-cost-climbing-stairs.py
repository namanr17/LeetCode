class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp_n_1, dp_n_2 = 0, 0
        
        for n in range(2, len(cost)+1):
            dp_n = min(dp_n_1 + cost[n-1], dp_n_2 + cost[n-2])
            dp_n_2, dp_n_1 = dp_n_1, dp_n
            
        return dp_n