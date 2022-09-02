# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:    
        self.count = 0
        covered = {None}
        
        def dfs(node, paren=None):
            if node.left:   dfs(node.left, node)
            if node.right:  dfs(node.right, node)
            
            if node.left not in covered or node.right not in covered:
                covered.update({node, paren, node.left, node.right})
                self.count += 1
                
        dfs(root)
        if root not in covered:
            self.count += 1
        
        return self.count