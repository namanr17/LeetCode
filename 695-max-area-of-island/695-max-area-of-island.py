class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            
            grid[i][j] = 0
            area = 1
            if i > 0 and grid[i-1][j]:
                area += dfs(i-1, j)
            if j > 0 and grid[i][j-1]:
                area += dfs(i, j-1)
            if i+1 < m and grid[i+1][j]:
                area += dfs(i+1, j)
            if j+1 < n and grid[i][j+1]:
                area += dfs(i, j+1)
            
            return area
                
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    maxArea = max(maxArea, dfs(i, j))
                    
        return maxArea