from functools import lru_cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        @lru_cache(None)
        def solve(i, j, k):
            if i == 0 and j == 0:
                return True if k == 0 else False
            elif k == 0:
                return False
            
            if i == 0:
                return True if s2[0:j] == s3[0:k] else False
            
            if j == 0:
                return True if s1[0:i] == s3[0:k] else False
            
            return (s1[i-1] == s3[k-1] and solve(i-1, j, k-1)) or (s2[j-1] == s3[k-1] and solve(i, j-1, k-1))
        
        return solve(len(s1), len(s2), len(s3))