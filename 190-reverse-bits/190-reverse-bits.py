class Solution:
    def reverseBits(self, n: int) -> int:
        INT_MAX = 2**32-1
        mask = 1
        ret = 0
        
        while(mask < INT_MAX):
            ret <<= 1
            if (n & mask):
                ret |= 1
            mask <<= 1
            
        return ret