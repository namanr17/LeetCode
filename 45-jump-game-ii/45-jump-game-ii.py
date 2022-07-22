class Solution:
    def jump(self, nums: List[int]) -> int:
        reach, lastJump, count = 0, 0, 0
        for i, n in enumerate(nums):
            if lastJump == len(nums)-1:
                break
            reach = max(reach, i + n)
            if i == lastJump:
                lastJump = reach
                count += 1

        return count