class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap, ans = [], []
        
        for i, (x, y) in enumerate(points):
            heappush(heap, [(x**2 + y**2)**0.5, i])
        
        for _, i in nsmallest(k, heap):
            ans.append(points[i])
            
        return ans