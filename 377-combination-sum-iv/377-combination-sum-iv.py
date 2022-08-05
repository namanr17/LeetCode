class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # from functools import lru_cache
        
        @lru_cache(None)
        def solve(t):
            if t < 0:
                return 0
            
            if t == 0:
                return 1
            
            ret = 0
            for num in nums:
                ret += solve(t - num)
            
            return ret
        
        return solve(target)