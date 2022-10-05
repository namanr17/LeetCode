class Solution:
    def numTilings(self, n: int) -> int:
        dp_prev = [0, 0, 0, 1]
        dp_curr = [0, 0, 0, 0]
        
        MOD = int(1e9) + 7
        
        for _ in range(n):
            dp_curr[0] = dp_prev[3] % MOD
            dp_curr[1] = (dp_prev[2] + dp_prev[0]) % MOD
            dp_curr[2] = (dp_prev[1] + dp_prev[0]) % MOD
            dp_curr[3] = (dp_prev[0] + dp_prev[1] + dp_prev[2] + dp_prev[3]) % MOD
            
            dp_prev = dp_curr[:]
        
        return dp_curr[3]