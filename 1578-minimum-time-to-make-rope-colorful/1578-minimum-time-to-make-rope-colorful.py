class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        last = 0
        
        colors += '_'
        
        for curr in range(1, len(colors)):
            if colors[curr] == colors[last]:
                continue
                
            toRemove = -inf
            while(last < curr):
                time += neededTime[last]
                toRemove = max(toRemove, neededTime[last])
                last += 1
            
            time -= toRemove
            
        return time
                
                
                