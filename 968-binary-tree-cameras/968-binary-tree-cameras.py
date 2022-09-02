# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:    
        count = 0
        
        def dfs(node):
            # 0 -> uncovered
            # 1 -> covered by a neighbour's camera
            # 2 -> covered by own camera
            
            nonlocal count
            
            # Leaf node is marked as uncovered
            if not node.left and not node.right:
                return 0
            
            # Consider child as covered by a neighbour if NULL
            left = dfs(node.left) if node.left else 1
            right = dfs(node.right) if node.right else 1
            
            # Place a camera if either child is uncovered
            if left == 0 or right == 0:
                count += 1
                return 2
            
            # No need to place a camera if both children are covered
            if left == 1 and right == 1:
                return 0
            
            # Node is covered if there's a camera at either child
            if left == 2 or right == 2:
                return 1
        
        if dfs(root) == 0:
            count += 1
        return count