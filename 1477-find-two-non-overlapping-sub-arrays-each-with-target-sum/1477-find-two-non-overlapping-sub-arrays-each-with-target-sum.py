class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefSum, winSum = {0: -1}, 0
        ans, best, best_till = inf, inf, [inf] * len(arr)
        
        for j in range(len(arr)):
            winSum += arr[j]
            
            if winSum - target in prefSum:
                i = prefSum[winSum - target]
                if i >= 0:
                    ans = min(ans, j - i + best_till[i])
                best = min(best, j - i)
            
            best_till[j] = best
            prefSum[winSum] = j
        
        return -1 if ans == inf else ans
            