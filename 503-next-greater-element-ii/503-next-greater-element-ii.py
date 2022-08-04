class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ngr = [-1] * len(nums)
        stack = deque(nums[::-1])
        
        for i in range(len(nums)-1, -1, -1):
            while(stack and stack[-1] <= nums[i]):
                stack.pop()
            if stack:
                ngr[i] = stack[-1]
            stack.append(nums[i])
            
        return ngr