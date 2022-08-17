class Solution:
    def minimumDeletions(self, s: str) -> int:
        ret = 0
        countb = 0
        for char in s:
            if countb and char == 'a':
                countb -= 1
                ret += 1
            elif char == 'b':
                countb += 1
        return ret