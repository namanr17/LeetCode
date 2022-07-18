class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, prefSum, m = 0, 0, {0:1}
        for num in nums:
            prefSum += num
            count += m.get(prefSum-k, 0)
            m[prefSum] = m.get(prefSum, 0) + 1
        return count
        