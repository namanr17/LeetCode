from math import gcd

class Solution:
    def distinctSequences(self, n: int) -> int:
        if n == 1:
            return 6
        
        dp = [[[0 for i in range(7)] for i in range(7)] for i in range(n+1)]
            
        for i in range(1, 7):
            for j in range(1, 7):
                if i != j and gcd(i, j) == 1:
                    dp[2][i][j] = 1
        
        for k in range(3, n+1):
            for i in range(1, 7):
                for j in range(1, 7):
                    if i != j and gcd(i, j) == 1:
                        for x in range(1, 7):
                            if x != i:
                                dp[k][i][j] += dp[k-1][j][x]
                        
        count = 0
        for i in range(1, 7):
            for j in range(1, 7):
                count += dp[n][i][j]
                
        return count % int(1e9 + 7)