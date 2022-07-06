class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        n_2 = 0
        n_1 = 1
        ans = 0
        for _ in range(1, n):
            ans = n_1 + n_2
            n_2 = n_1
            n_1 = ans
        
        return ans