class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        curr = [0] * n
        
        for i in range(m-1):
            curr[-1] = 1
            for j in range(n-2, -1, -1):
                curr[j] = curr[j+1] + dp[j]
            dp = curr
        
        return dp[0]
            