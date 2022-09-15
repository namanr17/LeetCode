class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:    return []

        count = Counter(changed)
        if count[0] % 2:    return []
        
        ret = []
        for k in sorted(count.keys()):
            while(0 < count[k] <= count[k*2]):
                ret.append(k)
                count[k] -= 1
                count[k*2] -= 1
            
            if count[k] > count[k*2]:
                return []
        
        return ret