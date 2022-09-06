class Solution:
    def shortestSubarray(self, A, K):
        N = len(A)
        
        # PrefSum
        B = [0] * (N + 1)
        for i in range(N): B[i + 1] = B[i] + A[i]
            
        # Monotonic Queue
        d = collections.deque()
        res = N + 1
        
        for i in range(N + 1):
            # Front of queue satisfies the prefSum condition (Subarray sum >= least K)
            while d and B[i] - B[d[0]] >= K: res = min(res, i - d.popleft())
                
            # Add current prefSum to the queue
            while d and B[i] <= B[d[-1]]: d.pop()
            d.append(i)
            
        return res if res <= N else -1
