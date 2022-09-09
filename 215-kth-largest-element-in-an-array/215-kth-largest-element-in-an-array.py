class Solution:
    def findKthLargest(self, nums, k):
        
        def RandomPart(l, r):
            p = random.randint(l, r)
            nums[p], nums[r] = nums[r], nums[p]
            
            m = l
            for i in range(l, r):
                if nums[i] < nums[r]:
                    nums[m], nums[i] = nums[i], nums[m]
                    m += 1
            
            nums[m], nums[r] = nums[r], nums[m]
            return m
        
        def QuickSelect(lo, hi, k):
            if lo == hi:    return nums[lo]
            
            pivot = RandomPart(lo, hi)
            rank = pivot - lo + 1
            
            if k < rank:
                return QuickSelect(lo, pivot - 1, k)
            elif k > rank:
                return QuickSelect(pivot + 1, hi, k - rank)
            else:   return nums[pivot]
            
        return QuickSelect(0, len(nums)-1, len(nums)-k+1)