class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        t_sum = 0
        for n in nums:
            if n % 2 == 0:
                t_sum += n
        
        ret = []
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                t_sum -= nums[idx]
                
            nums[idx] += val
            if nums[idx] % 2 == 0:
                t_sum += nums[idx]
            
            ret.append(t_sum)
        
        return ret