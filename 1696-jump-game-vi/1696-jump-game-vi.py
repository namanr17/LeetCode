from heapq import heappush, heappop

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        highestK = [(-nums[0],0)]
        result = nums[0]  # handles case where there is just 1 itme
        
        for i in range(1,len(nums)):
            while highestK[0][1] < i-k:
                heapq.heappop(highestK) # Pop the score whose index is out of range of i
            result = nums[i] + -highestK[0][0]  # Add highest possible score
            heapq.heappush(highestK, (-result,i))   # Append to heap

        return result