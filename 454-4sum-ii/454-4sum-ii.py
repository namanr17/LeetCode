class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        hm = defaultdict(int)
        
        for x in nums1:
            for y in nums2:
                hm[x + y] += 1
            
        
        for x in nums3:
            for y in nums4:
                count += hm[-(x+y)]
        
        return count