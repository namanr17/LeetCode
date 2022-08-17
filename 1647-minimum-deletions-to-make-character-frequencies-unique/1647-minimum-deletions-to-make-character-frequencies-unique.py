class Solution:
    def minDeletions(self, s: str) -> int:
        freq = sorted(Counter(s).values(), reverse=True)
        count = 0
        prev = freq[0]
        for i in range(1, len(freq)):
            if freq[i] >= prev:
                count += freq[i] - prev + 1
                freq[i] = prev - 1
            prev = freq[i] if freq[i] else prev
                
        return count