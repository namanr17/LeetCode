class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0
        
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        
        dp[-1] = 1
        
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
                continue
            
            dp[i] = dp[i+1] + dp[i+2] if i < n-1 and int(s[i:i+2]) < 27 else dp[i+1]
        
        return dp[0]