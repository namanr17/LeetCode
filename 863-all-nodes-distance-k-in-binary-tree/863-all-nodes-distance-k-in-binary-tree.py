# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj = defaultdict(list)
        
        def buildGraph(node):
            if node.left:
                adj[node.val].append(node.left.val)
                adj[node.left.val].append(node.val)
                buildGraph(node.left)
            if node.right:
                adj[node.val].append(node.right.val)
                adj[node.right.val].append(node.val)
                buildGraph(node.right)
            
        buildGraph(root)
        if len(adj) < k:
            return []
        
        q = Deque([(target.val, 0)])
        visited = [False] * len(adj)
        
        ans = []
        while(len(q)):
            u, d = q.popleft()
            visited[u] = True
            if d == k:
                ans.append(u)
            for v in adj[u]:
                if not visited[v]:
                    q.append((v, d + 1))
        
        return ans