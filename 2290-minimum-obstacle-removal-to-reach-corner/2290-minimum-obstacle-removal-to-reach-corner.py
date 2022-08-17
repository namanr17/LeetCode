class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        q = deque()
        cost = [[inf for _ in range(n)] for _ in range(m)]
        
        q.append((0, 0, 0))
        cost[0][0] = 0

        while(q):
            row, col, c = q.popleft()
    
            for nextRow, nextCol in [[row+1, col],[row, col+1],[row-1, col],[row, col-1]]:
                if 0 <= nextRow < m and 0 <= nextCol < n and cost[nextRow][nextCol] == inf:
                    if grid[nextRow][nextCol]:
                        cost[nextRow][nextCol] = c + 1
                        q.append((nextRow, nextCol, c + 1))
                    else:
                        cost[nextRow][nextCol] = c
                        q.appendleft((nextRow, nextCol, c))
        
        return cost[-1][-1]
                    
        