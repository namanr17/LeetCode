class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lo, hi = 0, len(arr)-k
        
        while(lo < hi):
            m = (lo + hi) // 2
            if x - arr[m] > arr[m+k] - x:
                lo = m + 1
            else:   hi = m
        
        return arr[lo : lo+k]