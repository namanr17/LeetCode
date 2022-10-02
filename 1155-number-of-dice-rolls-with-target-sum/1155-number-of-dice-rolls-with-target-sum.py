class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = int(1e9 + 7)
        
        @lru_cache(None)
        def solve(n, Sum):
            if n == 0 and Sum == 0:
                return 1
            
            if n == 0 or Sum == 0:
                return 0
            
            nonlocal k
            ret = 0
            for i in range(1, min(k, Sum)+1):                   
                ret += solve(n-1, Sum-i) % MOD
                ret %= MOD
            
            return ret
        
        return solve(n, target)