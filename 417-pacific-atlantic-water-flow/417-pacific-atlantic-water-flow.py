class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        
        def dfs_pacific(x, y):            
            toPacific.add((x, y))
            
            for (r, c) in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                if 0 <= r < rows and 0 <= c < cols and heights[r][c] >= heights[x][y]:
                    if (r, c) not in toPacific:
                        dfs_pacific(r, c)
            
        def dfs_atlantic(x, y):            
            toAtlantic.add((x, y))
            
            for (r, c) in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                if 0 <= r < rows and 0 <= c < cols and heights[r][c] >= heights[x][y]:
                    if (r, c) not in toAtlantic:
                        dfs_atlantic(r, c)
              
        toPacific = set()
        toAtlantic = set()
                        
        for r in range(rows):
            dfs_pacific(r, 0)
            dfs_atlantic(r, cols-1)
            
        for c in range(cols):
            dfs_pacific(0, c)
            dfs_atlantic(rows-1, c)
                    
        return list(toPacific & toAtlantic)