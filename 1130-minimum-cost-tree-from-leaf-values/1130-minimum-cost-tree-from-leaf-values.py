class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        dp = {}
        
        def solve(l, r):
            if l == r:
                return (0, arr[l])
            
            if (l, r) in dp:
                return dp[(l, r)]
            
            minCost, maxEle = float('inf'), 0
            for k in range(l, r):
                if (l, k) in dp:
                    cost_l, max_l = dp[(l, k)]
                else:   cost_l, max_l = solve(l, k)
                
                if (k+1, r) in dp:
                    cost_r, max_r = dp[(k+1, r)]
                else:   cost_r, max_r = solve(k+1, r)
                
                cost = max_l * max_r + cost_l + cost_r
                if cost < minCost:
                    minCost = cost
                    maxEle = max(max_l, max_r)
            
            dp[(l, r)] = (minCost, maxEle)
            return (minCost, maxEle)
        
        return solve(0, len(arr)-1)[0]