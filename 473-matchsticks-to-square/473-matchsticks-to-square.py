class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n, total = len(matchsticks), sum(matchsticks)
        if total % 4 != 0:
            return False
        
        subsets = [total // 4] * 4
        matchsticks = sorted(matchsticks)
        
        def backtrack(i):
            if i == 0 and sum(subsets) == 0:
                return True
            
            matchLen = matchsticks[i-1]
            for j in range(4):
                if subsets[j] - matchLen >= 0:
                    subsets[j] -= matchLen
                    if backtrack(i-1):
                        return True
                    subsets[j] += matchLen
        
        return backtrack(n)
                