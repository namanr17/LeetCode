class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        dist = []
        for n in arr:
            dist.append(abs(n - x))
        
        win_sum, start = sum(dist[0:k]), 0
        min_sum = win_sum
        for i in range(k, len(arr)):
            win_sum += dist[i] - dist[i-k]
            if win_sum < min_sum:
                min_sum = win_sum
                start = i-k+1
        
        return arr[start:start+k]