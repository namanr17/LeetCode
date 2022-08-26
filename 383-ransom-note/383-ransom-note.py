class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = Counter(magazine)
        for char in ransomNote:
            if not freq[char]:
                return False
            freq[char] -= 1
        return True