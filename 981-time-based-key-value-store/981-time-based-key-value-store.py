class TimeMap:

    def __init__(self):
        def store():
            return {'v' : [], 't' : []}
        
        self.M = defaultdict(store)

        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.M[key]['v'].append(value)
        self.M[key]['t'].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.M:
            return ''
        
        lo, hi = 0, len(self.M[key]['v'])
        
        while(lo < hi):
            mid = (lo + hi) // 2
            
            if self.M[key]['t'][mid] <= timestamp:
                lo = mid + 1
            else:   hi = mid
        
        return self.M[key]['v'][lo-1] if lo != 0 else ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)