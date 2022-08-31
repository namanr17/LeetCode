class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
            
        def dfs(x, y, visited):            
            visited.add((x, y))
            
            for (r, c) in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                if 0 <= r < rows and 0 <= c < cols and heights[r][c] >= heights[x][y]:
                    if (r, c) not in visited:
                        dfs(r, c, visited)
              
        toPacific = set()
        toAtlantic = set()
                        
        for r in range(rows):
            dfs(r, 0, toPacific)
            dfs(r, cols-1, toAtlantic)
            
        for c in range(cols):
            dfs(0, c, toPacific)
            dfs(rows-1, c, toAtlantic)
                    
        return list(toPacific & toAtlantic)