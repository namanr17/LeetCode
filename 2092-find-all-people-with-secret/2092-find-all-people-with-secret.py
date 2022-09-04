class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        adj = defaultdict(list)
        for x, y, time in meetings:
            adj[x].append((y, time))
            adj[y].append((x, time))
        
        visited = [inf for i in range(n)]
        
        def dfs(u, time):
            visited[u] = time
            
            for v, w in adj[u]:
                if visited[v] > w and w >= time:
                    dfs(v, w)
        
        dfs(0, 0)
        dfs(firstPerson, 0)
        
        return [i for i in range(n) if visited[i] != inf]