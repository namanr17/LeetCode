from functools import lru_cache
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
        
        @lru_cache(None)
        def solve(u, k):
            '''
            k = hop count (stops + 1)
            u = source node
            '''
            if u == dst:
                return 0
            if k == 0:
                return float('inf')
            
            adjNodes = adj[u] if u in adj.keys() else []
            minCost = float('inf')
            for (v, w) in adjNodes:
                minCost = min(minCost, w + solve(v, k-1))
            return minCost
        
        minCost = solve(src, k+1)
        return minCost if minCost != float('inf') else -1