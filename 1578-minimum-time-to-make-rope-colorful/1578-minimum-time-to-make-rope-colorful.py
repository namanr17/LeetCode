class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        last = 0
        
        colors += '_'
        
        for curr in range(1, len(colors)):
            if colors[curr] == colors[last]:
                continue
            
            if curr == last + 1:
                last = curr
                continue
            
            time += sum(neededTime[last:curr]) - max(neededTime[last:curr])
            last = curr
            
        # print(last, curr)
        return time
                
                
                