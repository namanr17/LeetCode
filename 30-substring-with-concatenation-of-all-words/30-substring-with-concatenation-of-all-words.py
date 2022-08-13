class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n, m = len(words), len(words[0])
        strLen, substrLen = len(s), n * m
        
        if strLen < substrLen:
            return []
        
        ret = []
        for i in range(strLen - substrLen + 1):
            BOW = Counter(words)
            substr = s[i:i+substrLen]
            
            for chunk in [substr[j:j+m] for j in range(0, substrLen, m)]:
                if not BOW[chunk]:  break
                BOW[chunk] -= 1
            
            if sum(BOW.values()) == 0:
                ret.append(i)
                
        return ret