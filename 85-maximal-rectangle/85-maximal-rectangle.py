class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        maxArea = float('-inf')
        heights = [0] * cols
        
        j = 0
        while(j < rows):
            stack = deque()
            nsl = [None] * cols
            nsr = [None] * cols
            
            for i in range(cols):
                heights[i] = heights[i] + 1 if int(matrix[j][i]) else 0
            
            for i in range(cols):
                while(stack and heights[stack[-1]] >= heights[i]):
                    stack.pop()
                nsl[i] = stack[-1] if stack else -1
                stack.append(i)
                
            stack.clear()
            for i in range(cols-1, -1, -1):
                while(stack and heights[stack[-1]] >= heights[i]):
                    stack.pop()
                nsr[i] = stack[-1] if stack else cols
                stack.append(i)
            
            for i in range(cols):
                width = nsr[i] - nsl[i] - 1
                maxArea = max(maxArea, heights[i]*width)
                
            # print(heights, nsl, nsr, maxArea)
            
            j += 1
        
        return maxArea