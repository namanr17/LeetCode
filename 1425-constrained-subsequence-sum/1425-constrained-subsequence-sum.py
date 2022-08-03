class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        heap = [(-nums[0], 0)]
        ans = nums[0]
        
        for i in range(1, len(nums)):
            while(heap[0][1] < i-k):
                heappop(heap)
            
            dp = nums[i] + max(0, -heap[0][0])
            heappush(heap, (-dp, i))
            ans = max(ans, dp)
                
        return ans
                