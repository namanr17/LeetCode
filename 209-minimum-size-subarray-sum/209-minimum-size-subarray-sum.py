class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        end = 0
        sum_ = 0
        ret_ = inf
        
        for start, num in enumerate(nums):
            sum_ += num
            while(end < len(nums) and sum_ >= target):
                ret_ = min(ret_, start - end + 1)
                sum_ -= nums[end]
                end += 1
            
        return ret_ if ret_ < inf else 0