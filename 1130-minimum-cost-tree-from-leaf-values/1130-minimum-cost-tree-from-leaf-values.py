class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        ngl = [None] * n
        ngr = [None] * n
        
        stack_ngl = deque()
        stack_ngr = deque()
        
        for i in range(n):
            while(stack_ngl and stack_ngl[-1] <= arr[i]):
                stack_ngl.pop()
            ngl[i] = stack_ngl[-1] if stack_ngl else float('inf')
            stack_ngl.append(arr[i])
            
            j = n - i - 1
            while(stack_ngr and stack_ngr[-1] < arr[j]):
                stack_ngr.pop()
            ngr[j] = stack_ngr[-1] if stack_ngr else float('inf')
            stack_ngr.append(arr[j])
            
        print(ngl, ngr)
        
        cost = 0
        for i in range(n):
            p = min(ngl[i], ngr[i])
            cost += arr[i] * p if p != float('inf') else 0
            
        return cost