class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        
        ans, diff = inf, inf
        nums.sort()
        
        for i, x in enumerate( nums[:-2] ):
            lo, hi = i+1, len(nums)-1
            
            curr = 0
            while lo < hi:
                curr = nums[lo] + nums[hi] + x
                
                if curr > target:
                    hi -= 1
                    while lo < hi and nums[hi] == nums[hi+1]:   hi -= 1
                elif curr < target:
                    lo += 1
                    while lo < hi and nums[lo] == nums[lo-1]:   lo += 1
                else:
                    return curr
                
                if abs( target - curr ) < diff:
                    ans, diff = curr, abs( target - curr )
        
        return ans