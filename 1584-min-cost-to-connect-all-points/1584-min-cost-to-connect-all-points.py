class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)
        
        for u in range(n):
            for v in range(n):
                if u != v:
                    w = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    adj[u] += [(v, w)]
        
        q = [(0, 0)]
        visited = [False] * n
        cost = 0
        
        for _ in range(n):
            (w, u) = heappop(q)
            while(visited[u]):
                (w, u) = heappop(q)
            visited[u] = True
            cost += w
            for (v, w) in adj[u]:
                if not visited[v]:
                    heappush(q, (w, v))
                
        # print(visited)
        # print(adj)
        # print(cost)
        
        return cost