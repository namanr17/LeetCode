class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ngr = {}
        stack = collections.deque()
        
        for num in nums2[::-1]:
            while(stack and stack[-1] < num):
                stack.pop()
                
            if stack:
                ngr[num] = stack[-1]
                
            stack.append(num)
            
        return [ngr.get(num, -1) for num in nums1]