# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def solve(node):
            if not node:
                return None
            
            if min(p.val, q.val) <= node.val <= max(p.val, q.val):
                return node
            
            if node.val < min(p.val, q.val):
                return solve(node.right)
            else:   return solve(node.left)
            
        return solve(root)