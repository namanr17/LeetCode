class Solution:
    mem = list(accumulate(range(100001), lambda s, i: (s << i.bit_length() | i) % 1000000007))
        
    def concatenatedBinary(self, n: int) -> int:
        return Solution.mem[n]
