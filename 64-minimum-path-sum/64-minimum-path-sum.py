class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        heap = [(grid[0][0], 0, 0)]
        cost = [[inf for _ in range(n)] for _ in range(m) ]
        cost[0][0] = grid[0][0]
        
        while(heap):
            W, x, y = heappop(heap)
        
            if (x, y) == (m-1, n-1):    break
            
            for x_next, y_next in [(x+1, y), (x, y+1)]:
                if x_next < m and y_next < n and cost[x_next][y_next] > cost[x][y] + grid[x_next][y_next]:
                    cost[x_next][y_next] = cost[x][y] + grid[x_next][y_next]
                    heappush(heap, (cost[x_next][y_next], x_next, y_next))
            
        return W