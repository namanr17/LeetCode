# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def prune(node):
            if not node:    return True
            
            pruneLeft, pruneRight = prune(node.left), prune(node.right)
            
            if pruneLeft:   node.left = None
            if pruneRight:  node.right = None
            
            return (node.val == 0) and pruneLeft and pruneRight
        
        if prune(root): return None
        return root