class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = defaultdict(int)
        for c in s:
            m[c] += 1
        for c in t:
            m[c] -= 1
        for f in m.values():
            if f:
                return False
        return True