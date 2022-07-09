class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for u, v, w in times:
            try:
                graph[u].append((v, w))
            except: graph[u] = [(v, w)]
            
        dist = [float('inf')] * n
        q = deque([])
        
        dist[k-1] = 0
        q.append(k)
        while(len(q)):
            u = q.pop()
            try:
                adjNodes = graph[u]
                for (v, w) in adjNodes:
                    if dist[v-1] > dist[u-1] + w:
                        dist[v-1] = dist[u-1] + w
                        q.append(v)
            except: pass
            
        d = max(dist)
        # print(graph, dist)
        return d if d != float('inf') else -1
            
        
        