from functools import lru_cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        @lru_cache(None)
        def solve(i, j, k):
            # print(f'called on {i, j, k}')
            if i == 0 and j == 0:
                if k == 0:
                    return True
                else:   return False
            elif k == 0:
                return False
            
            if i == 0 and s2[j-1] == s3[k-1]:
                return solve(i, j-1, k-1)
            
            if j == 0 and s1[i-1] == s3[k-1]:
                return solve(i-1, j, k-1)
            
            if i != 0 and j != 0:
                if s1[i-1] == s2[j-1] == s3[k-1]:
                    return solve(i-1, j, k-1) or solve(i, j-1, k-1)
                elif s1[i-1] == s3[k-1]:
                    return solve(i-1, j, k-1)
                elif s2[j-1] == s3[k-1]:
                    return solve(i, j-1, k-1)
            
            return False
        
        return solve(len(s1), len(s2), len(s3))