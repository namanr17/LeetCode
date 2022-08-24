class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        
        return n % 3 == 0 and self.isPowerOfThree(n // 3)