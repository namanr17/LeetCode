class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        q = deque()
            
        start, end = 0, 0
            
        while(start < len(nums)):
            
            # Inset into mono queue
            while(q and q[-1][1] < nums[start]):
                q.pop()
            q.append((start, nums[start]))
            start += 1
            
            # Skip if size of window < k
            if start - end < k:
                continue
            
            # Get max from mono queue
            ret.append(q[0][1])
            
            # Delete from mono queue
            while(q and q[0][0] <= end):
                q.popleft()
            end += 1
        
        return ret