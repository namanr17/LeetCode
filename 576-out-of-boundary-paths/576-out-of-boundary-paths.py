from functools import lru_cache

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def solve(i, j, leftMove):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 1
            
            if leftMove == 0:
                return 0
            
            return solve(i-1, j, leftMove-1) + solve(i, j-1, leftMove-1) + solve(i+1, j, leftMove-1) + solve(i, j+1, leftMove-1)
        
        return solve(startRow, startColumn, maxMove) % int(1e9+7)
                                                                                                             