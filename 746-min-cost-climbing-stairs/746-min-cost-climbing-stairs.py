class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp_n_1 = 0
        dp_n_2 = 0
        
        for n in range(2, len(cost)+1):
            dp_n = min(dp_n_1 + cost[n-1], dp_n_2 + cost[n-2])
            dp_n_2, dp_n_1 = dp_n_1, dp_n
            
        return dp_n
        
#         def solve(n):
#             if n == 0 or n == 1:
#                 return 0
            
#             return min(solve(n-1) + cost[n-1], solve(n-2) + cost[n-2])
        
#         return solve(len(cost))