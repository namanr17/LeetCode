class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        xor1, xor2 = 0, 0
        
        for n in arr1:
            xor1 ^= n
        
        for n in arr2:
            xor2 ^= n
        
        return xor1 & xor2