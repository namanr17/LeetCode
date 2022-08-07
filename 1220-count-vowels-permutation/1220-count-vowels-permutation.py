class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        adj = {
            0 : [1],
            1 : [0, 2],
            2 : [0, 1, 3, 4],
            3 : [2, 4],
            4 : [0]
         }
        
        dp = [1] * 5
        
        for _ in range(n-1):
            dp_next = [0] * 5
            for u in adj:
                for v in adj[u]:
                    dp_next[v] += dp[u]
            dp = dp_next
        
        return sum(dp) % int(1e9 + 7)