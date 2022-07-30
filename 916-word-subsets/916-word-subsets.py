class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans
        
        words2_max_freq = [0] * 26
        for word in words2:
            for c, freq in enumerate(count(word)):
                words2_max_freq[c] = max(words2_max_freq[c], freq)
                
        ans = []
        for word in words1:
            if all(x >= y for x, y in zip(count(word), words2_max_freq)):
                ans.append(word)
        
        return ans
                