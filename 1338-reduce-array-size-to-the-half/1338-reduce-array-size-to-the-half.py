class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = list(Counter(arr).values())
        count.sort(reverse=True)
        i, len_, sum_ = 0, 0, 0
        while(sum_ < len(arr) // 2):
            sum_ += count[i]
            len_ += 1
            i += 1
        return len_
        