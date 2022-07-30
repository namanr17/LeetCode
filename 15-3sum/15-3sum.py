class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n, nums = len(nums), sorted(nums)
        numSet, ans = {}, []
        
        for idx, num in enumerate(nums):
            if num in numSet:
                numSet[num][1] = idx
            else:   numSet[num] = [idx, idx]
            
        for i in range(n-2):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]:  continue
            l, r = i+1, n-1
            while(l < r):
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l = numSet[nums[l]][1] + 1
                elif s > 0:
                    r = numSet[nums[r]][0] -1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    l = numSet[nums[l]][1] + 1
                    r = numSet[nums[r]][0] - 1
            i = numSet[nums[i]][1]
            
        return ans