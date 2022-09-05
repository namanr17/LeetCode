class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0
        while(fast == 0 or fast != slow):
            fast = nums[nums[fast]]
            slow = nums[slow]
            
        match = fast
        fast, slow = nums[nums[0]], nums[match]
        while(slow != match):
            fast = nums[fast]
            slow = nums[slow]
        
        slow = nums[0]
        while(fast != slow):
            slow = nums[slow]
            fast = nums[fast]
            
        return fast