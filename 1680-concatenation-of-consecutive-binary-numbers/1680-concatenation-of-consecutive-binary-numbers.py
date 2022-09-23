class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return (self.concatenatedBinary(n-1) << n.bit_length() | n) % int(1e9 + 7) if n > 1 else 1