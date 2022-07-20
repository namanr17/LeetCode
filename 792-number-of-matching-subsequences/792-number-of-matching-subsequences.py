class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        m = {'':0}
        words = sorted(words, key=len)
        
        def find(suff: str) -> float:
            j = len(suff)
            while(suff[:j] not in m):
                j -= 1
            i = m[suff[:j]]
            while(i < len(s) and j < len(suff)):
                if s[i] == suff[j]:
                    j += 1
                    m[suff[:j]] = i+1
                i += 1
            if j != len(suff):
                m[suff] = float('inf')
            return m[suff]
        
        count = 0
        for word in words:
            if find(word) != float('inf'):
                count += 1
                
        # print(m)
        
        return count