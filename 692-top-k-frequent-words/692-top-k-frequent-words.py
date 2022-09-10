class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        buckets = defaultdict(list)
        
        maxFreq, ret = 0, []
        for word, freq in Counter(words).items():
            buckets[freq].append(word)
            maxFreq = max(maxFreq, freq)
            
        for i in range(maxFreq, 0, -1):
            currBucket = sorted(buckets[i])
            reqLen = min(k - len(ret), len(currBucket))
            ret.extend(currBucket[:reqLen])
        
        return ret