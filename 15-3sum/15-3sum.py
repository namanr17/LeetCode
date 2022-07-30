class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n, nums = len(nums), sorted(nums)
        numSet, ans = {}, set([])
        
        for idx, num in enumerate(nums):
            numSet[num] = idx
            
        for i in range(n-2):
            if nums[i] > 0: break
            for j in range(i+1, n-1):
                reqSum = -(nums[i] + nums[j])
                if reqSum in numSet.keys() and numSet[reqSum] > j:
                    ans.add(tuple(sorted([nums[i], nums[j], reqSum])))
                j = numSet[nums[j]]
            i = numSet[nums[i]]
        
        return ans