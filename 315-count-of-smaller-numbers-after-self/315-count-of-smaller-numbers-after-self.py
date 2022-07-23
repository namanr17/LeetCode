class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        class node:
            def __init__(self, idx, val):
                self.idx = idx
                self.val = val
        
        ans = [0] * len(nums)
        nodes = [node(i, num) for (i, num) in enumerate(nums)]
            
        def merge(start, mid, end):
            left, right, k = start, mid+1, 0
            out = [None] * (end-start+1)
            numsGreater = 0
            
            while(left <= mid and right <= end):
                if nodes[left].val <= nodes[right].val:
                    out[k] = nodes[left]
                    ans[nodes[left].idx] += numsGreater
                    left += 1
                else:
                    numsGreater += 1
                    out[k] = nodes[right]
                    right += 1
                k += 1
                
            while(left <= mid):
                out[k] = nodes[left]
                ans[nodes[left].idx] += numsGreater
                left, k = left+1, k+1
                
            while(right <= end):
                out[k] = nodes[right]
                right, k = right+1, k+1
            
            return out
        
        def solve(start, end):
            if start >= end:
                return
            
            mid = (end+start) // 2
            
            solve(start, mid)
            solve(mid+1, end)
            nodes[start:end+1] = merge(start, mid, end)
            
            return 
        
        solve(0, len(nums)-1)        
        return ans