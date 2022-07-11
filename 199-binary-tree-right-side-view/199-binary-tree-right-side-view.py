# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level = [None] * 100
         
        def solve(node, height):
            if not node:
                return 0
            
            level[height] = node.val
            left = solve(node.left, height+1) if node.left else 0
            right = solve(node.right, height+1) if node.right else 0
            
            return max(left, right)+1
         
        size = solve(root, 0)
        return level[:size]