class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ret = 0
        for i, num in enumerate(nums):
            ret ^= i ^ num
        return ret ^ n