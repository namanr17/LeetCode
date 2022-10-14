class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = -inf
        max_prod = min_prod = 1
        
        for num in nums:
            new_max = max(num, max_prod * num, min_prod * num)
            new_min = min(num, max_prod * num, min_prod * num)
            
            max_prod, min_prod = new_max, new_min
            ans = max(ans, max_prod)
            
        return ans