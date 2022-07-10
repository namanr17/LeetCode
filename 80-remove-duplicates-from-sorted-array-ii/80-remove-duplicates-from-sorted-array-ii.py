class Solution(object):
    def removeDuplicates(self, nums):
        if not nums: return 0
        slow = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
                if count > 2:
                    continue
            else:
                count = 1
            nums[slow] = nums[i]
            slow += 1
        return slow