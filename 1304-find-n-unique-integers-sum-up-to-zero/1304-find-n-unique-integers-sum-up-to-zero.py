class Solution:
    def sumZero(self, n: int) -> List[int]:
        ret = []
        
        if n % 2 != 0:
            ret.append(0)
            
        while(n // 2):
            ret.append(n)
            ret.append(-n)
            n -= 2
        
        return ret