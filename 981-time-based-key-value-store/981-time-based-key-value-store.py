class TimeMap:

    def __init__(self):    
        self.M = defaultdict(list)

        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.M[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.M:
            return ''
        
        lo, hi = 0, len(self.M[key])
        
        while(lo < hi):
            mid = (lo + hi) // 2
            
            if self.M[key][mid][0] <= timestamp:
                lo = mid + 1
            else:   hi = mid
        
        return self.M[key][lo-1][1] if lo != 0 else ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)