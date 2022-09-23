class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ret = 0
        
        for i in range(1, n+1):
            ret = ret << i.bit_length() | i
            ret = ret % int(1e9 + 7)
        
        return ret