class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        
        @lru_cache(None)
        def countTwoSum(target):
            count = 0
            for num in counter1:
                if target - num in counter2:
                    count += counter2[target - num] * counter1[num]
            return count
        
        counter3 = Counter(nums3)
        counter4 = Counter(nums4)
        
        count = 0
        for num3, num4 in product(counter3.keys(), counter4.keys()):
            count += countTwoSum(-(num3 + num4)) * counter3[num3] * counter4[num4]
        
        return count