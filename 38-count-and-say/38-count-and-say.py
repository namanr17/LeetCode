class Solution:
    @lru_cache(None)
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        say_prev = self.countAndSay(n-1)
        ret = ''
        count = 1
        for i in range(1, len(say_prev)):
            if say_prev[i] != say_prev[i-1]:
                ret += str(count) + say_prev[i-1]
                count = 1
            else:   count += 1
        
        return ret + str(count) + say_prev[-1]
            
        