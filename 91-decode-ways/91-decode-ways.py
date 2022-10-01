class Solution:
    def numDecodings(self, s: str) -> int:
        
        @lru_cache(None)
        def solve(i):
            if i >= len(s):
                return 1
            
            if s[i] == '0':
                return 0
            
            ret = 0
            
            ret += solve(i+1)
            ret += solve(i+2) if i+1 < len(s) and int(s[i:i+2]) <= 26 else 0
            
            return ret
        
        return solve(0)