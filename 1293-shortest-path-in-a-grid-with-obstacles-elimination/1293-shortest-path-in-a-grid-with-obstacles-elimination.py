class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if k > (m + n - 2):
            return m + n - 2
        
        q = deque([(0, 0, k)])
        visited = set([(0, 0, k)])
        count = 0
        
        while(q):
            l = len(q)
            while(l):
                (row, col, canEliminate), l = q.popleft(), l-1
                for (nextRow, nextCol) in [(row+1, col), (row, col+1), (row-1, col), (row, col-1)]:
                    if nextRow == m or nextCol == n or nextRow == -1 or nextCol == -1:
                        continue
                    
                    if grid[nextRow][nextCol]:
                        if canEliminate > 0 and (nextRow, nextCol, canEliminate-1) not in visited:
                            q.append((nextRow, nextCol, canEliminate-1))
                            visited.add((nextRow, nextCol, canEliminate-1))
                            
                    elif (nextRow, nextCol, canEliminate) not in visited:
                        if nextRow == m-1 and nextCol == n-1:
                            return count+1
                        q.append((nextRow, nextCol, canEliminate))
                        visited.add((nextRow, nextCol, canEliminate))
            count += 1
        
        return -1