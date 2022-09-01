class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 3
        if n == 2:
            return 8
        
        MOD = int(1e9) + 7
        
        P = [None] * (n+1)
        A = [None] * (n+1)
        L = [None] * (n+1)
        
        P[0], A[0], L[0] = 1, 1, 1
        P[1], A[1], L[1] = 1, 1, 1
        P[2], A[2], L[2] = 3, 2, 3
        
        for i in range(3, n+1):
            A[i] = (A[i-1] + A[i-2] + A[i-3]) % MOD
            P[i] = (P[i-1] + L[i-1] + A[i-1]) % MOD
            L[i] = (P[i-1] + A[i-1] + P[i-2] + A[i-2]) % MOD
            
        return (A[n] + P[n] + L[n]) % MOD
        