class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ret = []
        
        hs = {word: idx for idx, word in enumerate(words)}
        
        for i, word in enumerate(words):
            if not word:    continue
            if '' in hs and word[::-1] == word:
                ret.append([i, hs['']])
                ret.append([hs[''], i])
            if word[::-1] in hs:
                j = hs[word[::-1]]
                if i != j:
                    ret.append([i, j])
            for k in range(1, len(word)):
                pref, suff = word[:k], word[k:]
                if pref[::-1] in hs:
                    j = hs[pref[::-1]]
                    if suff == suff[::-1]:
                        ret.append([i, j])
                if suff[::-1] in hs:
                    j = hs[suff[::-1]]
                    if pref == pref[::-1]:
                        ret.append([j, i])
        
        return ret