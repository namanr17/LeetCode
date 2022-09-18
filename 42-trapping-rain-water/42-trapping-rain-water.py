class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        left, right = [0]*n, [0]*n
        
        left[0] = height[0]
        right[-1] = height[-1]
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])
            right[n-i-1] = max(right[n-i], height[n-i-1])
        
        water = 0
        for i, h in enumerate(height):
            water += min(left[i], right[i]) - h
        
        return water