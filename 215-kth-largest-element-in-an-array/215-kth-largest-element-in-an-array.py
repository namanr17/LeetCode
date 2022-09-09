class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        
        left = [n for n in nums if n > pivot]
        right = [n for n in nums if n < pivot]
        
        L, M = len(left), len(nums) - len(right) - len(left)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:   return pivot