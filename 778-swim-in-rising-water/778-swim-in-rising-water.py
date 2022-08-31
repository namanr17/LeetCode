class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(i, j, visited, threshold):
            visited[i][j] = True
            if (i, j) == (rows-1, cols-1):  return True
            
            for (x, y) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if not 0 <= x < rows or not 0 <= y < cols or visited[x][y]: continue
                if grid[x][y] <= threshold and dfs(x, y, visited, threshold):
                        return True
            return False
        
        def canReachDest(time):
            visited = [[False for _ in range(cols)] for _ in range(rows)]
            return dfs(0, 0, visited, time)
        
        lo, hi = grid[0][0], rows**2
        while(lo < hi):
            mid = (lo + hi) // 2
            if canReachDest(mid):
                hi = mid
            else:   lo = mid + 1
        
        return lo
                