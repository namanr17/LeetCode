class Solution:
    def minDeletions(self, s: str) -> int:
        freq = sorted(Counter(s).values(), reverse=True)
        count = 0
        prev = freq[0]
        for i in range(1, len(freq)):
            while(freq[i] >= prev):
                freq[i] -= 1
                count += 1
            prev = freq[i] if freq[i] else prev
                
        return count