class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        
        def insert_(idx, value):
            while(q and q[-1][1] < value):
                q.pop()
            q.append((idx, value))
        
        def delete_(idx):
            while(q and q[0][0] <= idx):
                q.popleft()
                
        def getMax_():
            return q[0][1]
        
        ret = []
        start, end = 0, 0
        while(start < k-1):
            insert_(start, nums[start])
            start += 1
            
        while(start < len(nums)):
            insert_(start, nums[start])
            ret.append(getMax_())
            
            delete_(end)
            
            start += 1
            end += 1
        
        return ret