class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n, m = len(words), len(words[0])
        strLen, substrLen = len(s), n * m
        
        if strLen < substrLen:
            return []
        
        ret = []
        bagOfWords = Counter(words)
        for i in range(strLen - substrLen + 1):
            BOW = bagOfWords.copy()
            substr = s[i:i+substrLen]
            
            flag = True
            for j in range(0, substrLen, m):
                chunk = substr[j:j+m]
                if not BOW[chunk]:
                    flag = False
                    break
                BOW[chunk] -= 1
            
            if flag and sum(BOW.values()) == 0:
                ret.append(i)
                
        return ret