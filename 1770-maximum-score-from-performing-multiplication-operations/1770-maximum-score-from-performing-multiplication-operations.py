class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        @lru_cache(2000)
        def solve(i, lo, hi):
            if i == len(multipliers):  return 0
            
            left = multipliers[i] * nums[lo] + solve(i+1, lo+1, hi)
            right = multipliers[i] * nums[hi] + solve(i+1, lo, hi-1)
            
            return max(left, right)
        
        m, n = len(multipliers), len(nums)
        return solve(0, lo=0, hi=n-1)