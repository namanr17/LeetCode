class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        nsl = [-1] * n 
        nsr = [n] * n
        
        stack, i = deque(), 0
        for i in range(n):
            while(stack and arr[stack[-1]] > arr[i]):
                stack.pop()
            if stack:
                nsl[i] = stack[-1]
            stack.append(i)
        
        stack.clear()
        for i in range(n-1, -1, -1):
            while(stack and arr[stack[-1]] >= arr[i]):
                stack.pop()
            if stack:
                nsr[i] = stack[-1]
            stack.append(i)
        
        ret = 0
        for i in range(n):
            ret += (i - nsl[i]) * (nsr[i] - i) * arr[i]
            
        # print(nsl)
        # print(nsr)
        
        return ret % int(1e9 + 7)