class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n, ans = len(nums), [-1, -1]
        if not n:
            return ans
        
        start, end = 0, n-1
        while(start <= end):
            mid = (start+end) // 2
            if nums[mid] > target:
                end = mid-1
            elif nums[mid] < target:
                start = mid+1
            else:   break
                
        if nums[mid] != target:
            return ans
        
        startLeft, endLeft = start, mid
        while(startLeft <= endLeft):
            midLeft = (startLeft+endLeft) // 2
            if midLeft > 0 and nums[midLeft-1] == target:
                endLeft = midLeft-1
            elif nums[midLeft] < target:
                startLeft = midLeft+1
            else:
                ans[0] = midLeft
                break
        
        startRight, endRight = mid, end
        while(startRight <= endRight):
            midRight = (startRight+endRight) // 2
            if midRight < end and nums[midRight+1] == target:
                startRight = midRight+1
            elif nums[midRight] > target:
                endRight = midRight-1
            else:
                ans[1] = midRight
                break

        return ans