# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        targets = set([p.val, q.val])
        
        def dfs(node):
            if not node:
                return None
            
            if node.val in targets:
                return node
            
            left, right = dfs(node.left), dfs(node.right)
            if left and right:
                return node
            
            return left or right
        
        return dfs(root)