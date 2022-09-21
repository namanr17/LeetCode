class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ret = []
        
        hs = {word[::-1]: idx for idx, word in enumerate(words)}
        
        for i, word in enumerate(words):
            if not word:    continue
                
            if '' in hs and word[::-1] == word:
                ret.append([i, hs['']])
                ret.append([hs[''], i])
                
            if word in hs and i != hs[word]:
                ret.append([i, hs[word]])
                
            for k in range(1, len(word)):
                pref, suff = word[:k], word[k:]
                
                if pref in hs and suff == suff[::-1]:
                    ret.append([i, hs[pref]])
                        
                if suff in hs and pref == pref[::-1]:
                    ret.append([hs[suff], i])
        
        return ret