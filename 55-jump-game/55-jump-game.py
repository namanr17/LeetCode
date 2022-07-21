class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i, n in enumerate(nums):
            if i > reach:
                break
            reach = max(reach, i + n)
        
        return True if reach >= len(nums)-1 else False