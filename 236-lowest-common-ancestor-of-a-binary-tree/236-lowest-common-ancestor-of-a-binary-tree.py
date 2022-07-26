# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if node.val == p.val or node.val == q.val:
            return node

        left = self.lowestCommonAncestor(node.left, p, q) if node.left else None
        right = self.lowestCommonAncestor(node.right, p, q) if node.right else None

        if left and right:
            return node
        return left or right