class Solution:
    def reverse(self, x: int) -> int:
        ret = 0
        
        sign_x = -1 if x < 0 else 1
        x = abs(x)
        
        while(x):
            ret *= 10
            ret += x % 10
            x = x // 10
            
        if -2**31 <= ret * sign_x <= 2**31-1:
            return ret * sign_x
        return 0
        