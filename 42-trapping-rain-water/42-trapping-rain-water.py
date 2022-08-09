class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        left = [0] * n
        right = [0] * n
        
        maxLeft, maxRight = 0, 0
        for i in range(n):
            maxLeft = max(maxLeft, height[i])
            left[i] = maxLeft
            
            maxRight = max(maxRight, height[n-i-1])
            right[n-i-1] = maxRight
        
        water = 0
        for i in range(n):
            water += min(left[i], right[i]) - height[i]
        
        return water