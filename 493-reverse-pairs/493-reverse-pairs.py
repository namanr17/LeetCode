class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        def mergeAndCount(l, mid, r):
            leftArr = [nums[i] for i in range(l, mid+1)]
            rightArr = [nums[i] for i in range(mid+1, r+1)]
            
            i, j, k = 0, 0, l
            p, count = 0, 0
            
            while(i < len(leftArr)):
                while(p < len(rightArr) and leftArr[i] > 2*rightArr[p]):
                    p += 1
                count += p
                
                while(j < len(rightArr) and leftArr[i] >= rightArr[j]):
                    nums[k] = rightArr[j]
                    j += 1
                    k += 1
                
                nums[k] = leftArr[i]
                k += 1
                i += 1
                
            while(j < len(rightArr)):
                nums[k] = rightArr[j]
                k += 1
                j += 1
            
            return count
            
        
        def mergeSortAndCount(l, r):
            if l >= r:
                return 0
            
            mid = (l + r) // 2
            
            leftCount = mergeSortAndCount(l, mid)
            rightCount = mergeSortAndCount(mid+1, r)
            
            totalCount = mergeAndCount(l, mid, r)
            
            return totalCount + leftCount + rightCount
        
        return mergeSortAndCount(0, len(nums)-1)