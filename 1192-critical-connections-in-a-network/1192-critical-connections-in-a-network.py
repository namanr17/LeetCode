class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
            
        ids = [0] * n
        low = [0] * n
        visited = [False] * n
        
        def dfs(u, parent, id_):
            visited[u] = True
            ids[u] = low[u] = id_
            
            for v in adj[u]:
                if v == parent: continue
                if not visited[v]:
                    dfs(v, u, id_+1)
                    low[u] = min(low[u], low[v])
                    if ids[u] < low[v]:
                        bridges.append([u, v])
                else:   low[u] = min(low[u], ids[v])
        
        bridges = []
        for i in range(n):
            if not visited[i]:
                dfs(i, None, 0)
        
        return bridges