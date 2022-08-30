class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        
        start = 0
        for r in range(rows):
            for c in range(cols):   
                start |= mat[r][c] << (r * cols + c)
        
        dq = deque([(start, 0)])
        visited = {start}
        
        while(dq):
            state, steps = dq.popleft()
            if not state:  return steps
            
            for r in range(rows):
                for c in range(cols):
                    next_state = state
                    for (x, y) in (r, c), (r+1, c), (r-1, c), (r, c-1), (r, c+1):
                        if 0 <= x < rows and 0 <= y < cols:
                            next_state ^= 1 << (x * cols + y)
                            
                    if next_state not in visited:
                        dq.append((next_state, steps+1))
                        visited.add(next_state)
            
        return -1