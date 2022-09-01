class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 3
        
        dp = [None for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 2
        dp[2] = 4
        
        MOD = int(1e9) + 7
        
        for i in range(3, n+1):
            dp[i] =  (dp[i-1] + dp[i-2] + dp[i-3]) % MOD
            
        ret = dp[n]
        for i in range(n):
            ret += (dp[i] * dp[n-i-1]) % MOD
            ret = ret % MOD
            
        return ret