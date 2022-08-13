class Solution:
    def reverse(self, x: int) -> int:
        ret = 0
        
        sign_x = -1 if x < 0 else 1
        x = abs(x)
        MOD = 2**31
        if sign_x > 0:
            MOD -= 1
        
        while(x != 0):
            prev = ret
            ret *= 10
            ret = (ret + x % 10) % MOD
            x = x // 10
            
            if ret // 10 != prev:
                return 0
            
            
        return sign_x * ret