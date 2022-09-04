# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node, r, c):
            M[c].append((r, node.val))
            
            if node.left:   dfs(node.left, r+1, c-1)
            if node.right:  dfs(node.right, r+1, c+1)
            
        M, ret = defaultdict(list), []
        dfs(root, 0, 0)
        
        for c in sorted(M):
            nodes = sorted(M[c], key=lambda x: (x[0], x[1]))
            ret.append([val for (r, val) in nodes])
        
        return ret
        