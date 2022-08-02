class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        def countLessOrEqual(k):
            r, c = 0, n-1
            count = 0 
            while(r < n and c >= 0):
                if matrix[r][c] <= k:
                    count += c+1
                    r += 1
                else:   c -= 1
            
            return count
        
        lo, hi = matrix[0][0], matrix[n-1][n-1]
        while(lo < hi):
            mid = (lo + hi) // 2
            if countLessOrEqual(mid) < k:
                lo = mid + 1
            else:   hi = mid
        
        return lo