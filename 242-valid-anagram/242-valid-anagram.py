class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = defaultdict(int)
        if len(s) != len(t):
            return False
        for c in s:
            m[c] += 1
        for c in t:
            m[c] -= 1
            if m[c] < 0:
                return False
        return True