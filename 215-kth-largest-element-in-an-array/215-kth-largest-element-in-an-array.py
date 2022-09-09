class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        
        M = 0
        left, right = [], []
        
        for n in nums:
            if n > pivot:
                left.append(n)
            elif n < pivot:
                right.append(n)
            else:   M += 1
        
        L = len(left)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:   return pivot