class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ngr = {}
        stack = collections.deque()
        
        for num in nums2[::-1]:
            while(len(stack) and stack[-1] < num):
                stack.pop()
                
            if len(stack):
                ngr[num] = stack[-1]
            else:   ngr[num] = -1
                
            stack.append(num)
            
        return [ngr[num] for num in nums1]