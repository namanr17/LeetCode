from functools import lru_cache

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        @lru_cache(None)
        def solve(i, target, prevColor):
            # print(i, target, prevColor)
            if i == 0:
                return 0 if target == 0 else float('inf')
            
            if target < 0:
                return float('inf')
            
            if houses[i-1] == 0:
                minCost = float('inf')
                for color in range(1, n+1):
                    newTarget = target if color == prevColor else target - 1
                    minCost = min(minCost, cost[i-1][color-1] + solve(i-1, newTarget, color))
            else:
                newTarget = target if houses[i-1] == prevColor else target - 1
                minCost = solve(i-1, newTarget, houses[i-1])
                
            return minCost
        
        minCost = solve(m, target, 0)
        return minCost if minCost != float('inf') else -1