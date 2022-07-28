from functools import lru_cache
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        
        @lru_cache(None)
        def solve(S, n, i):
            if S == 0 and n == 0:
                return True
            
            if i == 0 or n == 0 or S < 0:
                return False
            
            if nums[i-1] <= S:
                return solve(S-nums[i-1], n-1, i-1) or solve(S, n, i-1)
            
            return solve(S, n, i-1)
        
        S_, n_ = sum(nums), len(nums)
        for k in range(1, n_):
            if (S_ * k) % n_ == 0 and solve((S_ * k) // n_, k, len(nums)):
                return True
            
        return False