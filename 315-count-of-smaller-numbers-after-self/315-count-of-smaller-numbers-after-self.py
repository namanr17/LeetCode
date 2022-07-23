class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        class node:
            def __init__(self, idx, val):
                self.idx = idx
                self.val = val
        
        ans = [0] * len(nums)
        m = [node(i, num) for (i, num) in enumerate(nums)]
            
        def merge(left, right):
            i, j, k = 0, 0, 0
            out = [None] * (len(left) + len(right))
            numsGreater = 0
            
            while(i < len(left) and j < len(right)):
                if left[i].val <= right[j].val:
                    out[k] = left[i]
                    ans[left[i].idx] += numsGreater
                    i += 1
                else:
                    numsGreater += 1
                    out[k] = right[j]
                    j += 1
                k += 1
                
            while(i < len(left)):
                out[k] = left[i]
                ans[left[i].idx] += numsGreater
                i += 1
                k += 1
                
            while(j < len(right)):
                out[k] = right[j]
                j += 1
                k += 1
                
            return out
        
        def solve(arr):
            if len(arr) < 2:
                return arr
            
            mid = len(arr) // 2
            left = solve(arr[:mid])
            right = solve(arr[mid:])
            
            return merge(left, right)
        
        solve(m)        
        return ans