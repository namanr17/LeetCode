class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pq, visited, time = [(grid[0][0], 0, 0)], set([(0, 0)]), 0
        
        while(pq):
            w, i ,j = heappop(pq)
            time = max(time, w)
            
            if i == j == n-1:   break

            for (x, y) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if not 0 <= x < n or not 0 <= y < n or (x, y) in visited: continue
                heappush(pq, (grid[x][y], x, y))
                visited.add((x, y))
                
        return time