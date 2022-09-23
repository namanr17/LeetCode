class Solution:
    def concatenatedBinary(self, n: int) -> int:
        if n == 1:  return 1
        
        return (self.concatenatedBinary(n-1) << n.bit_length() | n) % int(1e9 + 7)