class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        dp = {n : 1 for n in arr}
        arr = sorted(arr)
        
        ret = 0
        for i, n in enumerate(arr):
            for m in arr[:i]:
                if n % m == 0 and n // m in dp:
                    dp[n] += dp[m] * dp[n // m]
            
            ret += dp[n] % int(1e9 + 7)
        
        return ret % int(1e9 + 7)