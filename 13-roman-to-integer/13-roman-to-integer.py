class Solution:
    def romanToInt(self, s: str) -> int:
        mapInt = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        ret = 0
        prev = 0
        for r in s:
            curr = mapInt[r]
            if curr > prev:
                ret += curr - 2*prev
            else:
                ret += curr
            prev = curr
        return ret