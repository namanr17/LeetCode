class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        q = [(0, 0)]
        visited = [False] * n
        cost = 0
        
        for _ in range(n):
            (w, u) = heappop(q)
            while(visited[u]):
                (w, u) = heappop(q)
            visited[u] = True
            cost += w
            for v in range(n):
                if not visited[v]:
                    w = abs(points[v][0] - points[u][0]) + abs(points[v][1] - points[u][1])
                    heappush(q, (w, v))
        
        return cost