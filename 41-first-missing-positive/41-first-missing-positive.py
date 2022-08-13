class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        
        for i, num in enumerate(nums):
            nums[i] = num if 0 < num < n else 0
            
        for num in nums:
            nums[num % n] += n
                
        for i in range(1, n):
            if nums[i] < n:
                return i
        
        return n