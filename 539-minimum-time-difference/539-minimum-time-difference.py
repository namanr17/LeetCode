class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        arr = [int(time.split(':')[0]) * 60 + int(time.split(':')[1]) for time in timePoints]
        arr.sort()
        
        ret = 24*60 - arr[-1] + arr[0]
        for i in range(1, len(arr)):
            ret = min(ret, arr[i] - arr[i-1])
        
        return ret
        