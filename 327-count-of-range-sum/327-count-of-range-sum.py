class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefSum = [0] * (len(nums)+1)
        for i in range(len(nums)):
            prefSum[i+1] = prefSum[i] + nums[i]
            
        def solve(l, r):
            if l == r:
                return 0
            
            mid = (l + r) // 2
            count = solve(l, mid) + solve(mid+1, r)
            
            i, j, k = l, mid+1, mid+1
            while(i <= mid):
                while(j <= r and prefSum[j] < lower + prefSum[i]):
                    j += 1
                while(k <= r and prefSum[k] <= upper + prefSum[i]):
                    k += 1
                count += k - j
                i += 1
            
            prefSum[l:r+1] = sorted(prefSum[l:r+1])
            return count
        
        return solve(0, len(nums))