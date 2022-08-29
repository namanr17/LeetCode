# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:    return False
        
        def dfs(node, tSum):
            if not node:    return False
            
            tSum -= node.val
            if not node.left and not node.right and not tSum:
                return True
            
            return dfs(node.left, tSum) or dfs(node.right, tSum)
        
        return dfs(root, targetSum)
                