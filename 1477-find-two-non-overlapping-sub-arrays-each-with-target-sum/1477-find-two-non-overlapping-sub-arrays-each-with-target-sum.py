class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        i, window, result = 0, 0, float('inf')
        premin = [float('inf')] * len(arr)
        for j, num in enumerate(arr):
            window += num
            while window > target:
                window -= arr[i]
                i += 1
            if window == target:
                curr = j - i + 1
                result = min(result, curr + premin[i - 1])
                premin[j] = min(curr, premin[j - 1])
            else:
                premin[j] = premin[j - 1]
        return result if result < float('inf') else -1
