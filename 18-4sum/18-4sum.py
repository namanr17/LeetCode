class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        def twoSum(nums, target):
            ret, hs = [], {None}
            
            for n in nums:
                if ret and ret[-1][1] == n: continue
                    
                if target - n in hs:
                    ret.append([target - n, n])
                    
                hs.add(n)
            
            return ret
        
        def kSum(nums, k, target):
            res = []
            
            if not nums:
                return res
            
            if nums[0] > target // k or nums[-1] < target // k:
                return res
             
            if k == 2:
                return twoSum(nums, target)
            
            for idx in range(len(nums)):
                if idx and nums[idx] == nums[idx - 1]:    continue
                    
                for ans in kSum(nums[idx + 1:], k - 1, target - nums[idx]):
                    res.append(ans + [nums[idx]])
            
            return res
        
        return kSum(nums, 4, target)
            
            