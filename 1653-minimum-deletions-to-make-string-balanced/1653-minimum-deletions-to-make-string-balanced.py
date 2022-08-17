class Solution:
    def minimumDeletions(self, s: str) -> int:
        a, b, cnt = s.count('a'), 0, len(s)
        for c in s:
            if c == 'b':
                cnt = min(cnt, a + b)
                b += 1
            else:
                a -= 1
        return min(cnt, b)