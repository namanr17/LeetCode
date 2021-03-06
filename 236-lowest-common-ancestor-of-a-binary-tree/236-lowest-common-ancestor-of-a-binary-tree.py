# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node.val == p.val or node.val == q.val:
                return node
            
            left = dfs(node.left) if node.left else None
            right = dfs(node.right) if node.right else None
            
            if left and right:
                return node
            return left or right
        
        return dfs(root)