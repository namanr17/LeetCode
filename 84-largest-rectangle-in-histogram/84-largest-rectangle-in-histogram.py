class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def pair():
            return [None, None]
        
        nslr = defaultdict(pair)
        
        stack = deque()
        for i in range(len(heights)):
            while(stack and heights[stack[-1]] >= heights[i]):
                stack.pop()
            nslr[i][0] = stack[-1] if stack else -1
            stack.append(i)
        
        stack.clear()
        for i in range(len(heights)-1, -1, -1):
            while(stack and heights[stack[-1]] >= heights[i]):
                stack.pop()
            nslr[i][1] = stack[-1] if stack else len(heights)
            stack.append(i)
        
        maxArea = float('-inf')
        for i, [left, right] in nslr.items():
            maxArea = max(maxArea, heights[i] * (right - left - 1))
        
        return maxArea