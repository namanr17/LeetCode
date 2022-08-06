class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        @lru_cache(None)
        def solve(l, r):
            if l == r:
                return 0, arr[l]
            
            minCost, maxEle = float('inf'), 0
            for k in range(l, r):
                cost_l, max_l = solve(l, k)
                cost_r, max_r = solve(k+1, r)
                
                cost = max_l * max_r + cost_l + cost_r
                if cost < minCost:
                    minCost = cost
                    maxEle = max(max_l, max_r)
            
            return minCost, maxEle
        
        return solve(0, len(arr)-1)[0]