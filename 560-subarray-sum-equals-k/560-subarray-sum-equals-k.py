class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = [n for n in nums]
        for i in range(1, len(nums)):
            prefix[i] += prefix[i-1]
                
        m = {}
        for pref in prefix:
            if pref == k:
                count += 1
                
            if pref - k in m.keys():
                count += m[pref-k]
            
            if pref in m.keys():
                m[pref] += 1
            else:   m[pref] = 1
                
        return count
        