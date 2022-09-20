class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            return self.longestCommonSubsequence(text2, text1)
        
        len1, len2 = len(text1), len(text2)
        dp, dp_prev = [0] * (len2+1), [0] * (len2+1)
        
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                
                if text1[i-1] == text2[j-1]:
                    dp[j] = dp_prev[j-1] + 1
                else:   dp[j] = max(dp_prev[j], dp[j-1])
            
            dp_prev = dp[:]
        
        return dp[-1]