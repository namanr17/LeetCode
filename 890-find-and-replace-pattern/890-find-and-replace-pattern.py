class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        
        for word in words:
            m, matchCount, processed = {}, 0, set([])
            for i, c in enumerate(pattern):
                if c not in m.keys() and word[i] not in processed:
                    m[c] = word[i]
                    processed.add(word[i])
                    matchCount += 1
                elif c in m.keys() and m[c] == word[i]:
                    matchCount += 1
                else:   break
                
            if matchCount == len(pattern):
                ans.append(word)
                
        return ans