class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket, maxFreq = defaultdict(list), -inf
        
        for num, freq in Counter(nums).items():
            bucket[freq].append(num)
            maxFreq = max(maxFreq, freq)
            
        ret = []
        for f in range(maxFreq, 0, -1):
            if len(ret) + len(bucket[f]) > k:
                req = k - len(ret)
                ret.extend(bucket[f][:req])
                break
            ret.extend(bucket[f])
            
        return ret