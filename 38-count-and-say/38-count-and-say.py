class Solution:
    @lru_cache(None)
    def countAndSay(self, n):
        if n == 1:  return "1"
        
        s = self.countAndSay(n-1)
        return ''.join(str(len(list(group))) + digit for digit, group in itertools.groupby(s))
            
        