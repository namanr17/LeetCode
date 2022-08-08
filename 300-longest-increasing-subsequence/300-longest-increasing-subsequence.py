class Solution:

    def init_segTree(self, l, r, idx=1):
        self.lo[idx], self.hi[idx] = l, r
        self.val[idx] = 0

        if l == r:
            return

        mid = (l + r) // 2
        self.init_segTree(l, mid, idx*2)
        self.init_segTree(mid+1, r, idx*2+1)

        return
    
    
    def query(self, l, r, idx=1):
        if l > r:   return 0
        
        if l == self.lo[idx] and r == self.hi[idx]:
            return self.val[idx]
        
        mid = (self.lo[idx] + self.hi[idx]) // 2
        if r <= mid:
            return self.query(l, r, 2*idx)
        elif l > mid:
            return self.query(l, r, 2*idx+1)
        else:
            return max(self.query(l, mid, 2*idx), self.query(mid+1, r, 2*idx+1))
        
        
    def insert(self, k, lis, idx=1):
        if self.lo[idx] == self.hi[idx] == k:
            self.val[idx] = lis
            return
        
        mid = (self.lo[idx] + self.hi[idx]) // 2
        if k <= mid:
            self.insert(k, lis, 2*idx)
        else:   self.insert(k, lis, 2*idx+1)
            
        self.val[idx] = max(self.val[2*idx], self.val[2*idx+1])
        return
    
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        self.lo = [None] * (4*n+1)
        self.hi = [None] * (4*n+1)
        self.val = [None] * (4*n+1)
        
        self.init_segTree(0, n-1)
        
        idxSorted = {num : i for (i, num) in enumerate(sorted(nums))}
        
        for num in nums:
            k = idxSorted[num]
            lis = self.query(0, k-1) + 1
            self.insert(k, lis)
        
        return self.query(0, n-1)