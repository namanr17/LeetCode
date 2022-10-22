class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        required = len(t)
        i = 0
        I, J = 0, 0
        for j, char in enumerate(s, 1):
            if need[char] > 0:
                required -= 1
                
            need[char] -= 1
            if not required:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J -I:
                    I, J = i, j
                
        return s[I:J]
                