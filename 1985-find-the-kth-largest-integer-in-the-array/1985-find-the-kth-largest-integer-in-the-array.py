class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:        
        nums = sorted(nums, key=lambda x:[len(x), int(x)], reverse=True)
        return nums[k-1]