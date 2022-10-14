class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = -inf
        max_till_here = 0
        
        for num in nums:
            max_till_here += num
            max_so_far = max(max_so_far, max_till_here)
            
            if max_till_here < 0:
                max_till_here = 0
            
        return max_so_far