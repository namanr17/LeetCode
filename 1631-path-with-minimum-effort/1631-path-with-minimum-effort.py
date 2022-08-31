class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        
        heap = [(0, rows-1, cols-1)]
        cost = [[inf for _ in range(cols)] for _ in range(rows)]
        cost[rows-1][cols-1] = 0
        
        while(heap):
            w, r, c = heappop(heap)
            if w > cost[r][c]:
                continue
            
            if not r | c:
                return w
            
            for (x, y) in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                if 0 <= x < rows and 0 <= y < cols:
                    update = max(w, abs(heights[x][y] - heights[r][c]))
                    if cost[x][y] > update:
                        cost[x][y] = update
                        heappush(heap, (update, x, y))
            