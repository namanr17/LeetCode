class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        if len(s) <= k:
            return 0
        
        if len(s) < 3:
            return len(s)
        
        @lru_cache(None)
        def solve(idx, prevChar, prevCharCount, canDelete):
            if canDelete < 0:
                return inf
            
            if idx >= len(s):
                return 0
            
            if s[idx] == prevChar:
                inc = 1 if prevCharCount in {1, 9, 99} else 0
                return solve(idx + 1, prevChar, prevCharCount + 1, canDelete) + inc
            
            deleteCurrChar = solve(idx + 1, prevChar, prevCharCount, canDelete - 1)
            keepCurrChar = solve(idx + 1, s[idx], 1, canDelete) + 1

            return min(deleteCurrChar, keepCurrChar)
            
        return solve(0, "", 0, k)