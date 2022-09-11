class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = [(efficiency[i], speed[i]) for i in range(n)]
        engineers.sort(key = lambda x:(-x[0], x[1]))
        
        heap = []
        MOD = int(1e9) + 7
        maxPerf, total_s = 0, 0
        
        for e, s in engineers:
            if len(heap) == k:
                total_s -= heappop(heap)
                
            total_s += s
            heappush(heap, s)
            
            maxPerf = max(maxPerf, e * total_s)
        
        return maxPerf % MOD