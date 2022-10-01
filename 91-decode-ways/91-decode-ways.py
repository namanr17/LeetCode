class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0
        
        n = len(s)
        
        dp, dp_1, dp_2 = 0, 1, 1
        
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                dp = 0
            else:   dp = dp_1 + dp_2 if i < n-1 and int(s[i:i+2]) < 27 else dp_1
            
            dp_1, dp_2 = dp, dp_1
        
        return dp