# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, hi):
            count = 0
            if node.val >= hi:
                count = 1
                hi = node.val
            
            count += dfs(node.left, hi) if node.left else 0
            count += dfs(node.right, hi) if node.right else 0
            
            return count
        
        return dfs(root, -inf)