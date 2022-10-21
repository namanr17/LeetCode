class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hs = defaultdict(int)
        
        for i, n in enumerate(nums):
            if n in hs and abs(hs[n] - i) <= k:
                return True
            hs[n] = i
        
        return False