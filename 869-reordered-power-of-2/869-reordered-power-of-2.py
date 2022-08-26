class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digitsFreq = Counter(str(n))
        return any(digitsFreq == Counter(str(1<<i)) for i in range(30))