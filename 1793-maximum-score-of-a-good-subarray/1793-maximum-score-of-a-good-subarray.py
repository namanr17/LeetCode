class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def pair():
            return [None, None]
        
        nsrl = defaultdict(pair)
        stack = deque()
        
        for i in range(n):
            while(stack and nums[stack[-1]] >= nums[i]):
                stack.pop()
            nsrl[i][0] = stack[-1] if stack else -1
            stack.append(i)
        
        stack.clear()
        for i in range(n-1, -1, -1):
            while(stack and nums[stack[-1]] >= nums[i]):
                stack.pop()
            nsrl[i][1] = stack[-1] if stack else n
            stack.append(i)
        
        maxScore = float('-inf')
        for i, [l, r] in nsrl.items():
            if l < k < r:
                maxScore = max(maxScore, (r-l-1)*nums[i])
            
        return maxScore