class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words2_max_freq = defaultdict(int)
        for word in words2:
            for c, freq in Counter(word).items():
                words2_max_freq[c] = max(words2_max_freq[c], freq)
                
        ans = []
        for word in words1:
            flag = True
            wordFreq = Counter(word)
            for c, freq in words2_max_freq.items():
                if freq > wordFreq[c]:
                    flag = False
                    break
            if flag:
                ans.append(word)
        
        return ans
                