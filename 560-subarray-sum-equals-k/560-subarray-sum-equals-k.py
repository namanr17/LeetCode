class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, prefSum = 0, 0
                
        m = {0:1}
        for num in nums:
            prefSum += num
                
            if prefSum - k in m.keys():
                count += m[prefSum-k]
            
            if prefSum in m.keys():
                m[prefSum] += 1
            else:   m[prefSum] = 1
                
        return count
        