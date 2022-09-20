class Solution:  # 4724 ms, faster than 34.98%
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) < len(nums2): 
            return self.findLength(nums2, nums1)  # Make sure len(nums1) > len(nums2) to optimize space
        m, n = len(nums1), len(nums2)
        dp, prevDP = [0] * (n+1), [0] * (n+1)
        ans = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[j] = prevDP[j-1] + 1
                else:
                    dp[j] = 0
                ans = max(ans, dp[j])
            dp, prevDP = prevDP, dp
        return ans