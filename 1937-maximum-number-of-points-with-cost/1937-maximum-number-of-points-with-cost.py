class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        
        if rows == 1:   return max(points[0])
        if cols == 1:   return sum(points[i][0] for i in range(rows))
        
        prev = points[0]
        dp, left, right = [None] * cols, [None] * cols, [None] * cols
        for r in range(1, rows):
            left[0] = prev[0]
            for i in range(1, cols):
                left[i] = max(left[i-1]-1, prev[i])
            
            right[-1] = prev[-1]
            for i in range(cols-2, -1, -1):
                right[i] = max(right[i+1]-1, prev[i])
            
            for i in range(cols):
                dp[i] = points[r][i] + max(left[i], right[i])
            prev = dp
            
        return max(dp)