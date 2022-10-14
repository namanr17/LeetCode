class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = -inf
        dp_prev_max = dp_prev_min = 1
        
        for num in nums:
            dp_max = max(num, dp_prev_max * num, dp_prev_min * num)
            dp_min = min(num, dp_prev_max * num, dp_prev_min * num)
            
            dp_prev_min, dp_prev_max = dp_min, dp_max
            ans = max(ans, dp_max)
            
        return ans